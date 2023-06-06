import argparse
import copy
import importlib
import sys
import time

import hid

import usb_hid_keys


VERBOSE = False


def print_device_dict(device_dict):
    print(f"Manufacturer: {device_dict['manufacturer_string']}")
    print(f"Product: {device_dict['product_string']}")
    print(f"Path: {device_dict['path']}")
    print(f"vendor_id, product_id: {device_dict['vendor_id']},{device_dict['product_id']}")
    print(f"Interface: {device_dict['interface_number']}")
    print()

def list_devices(ids):
    for device_dict in filter_device_dicts(hid.enumerate(), ids):
        # Filter for keyboards
        if device_dict["product_string"] in ["Varmilo Keyboard", "USB-HID Keyboard"]:
            print_device_dict(device_dict)

def filter_device_dicts(dicts, ids):
    set_vid, set_pid = ids
    device_filter = lambda d: \
        (
            (not set_vid) \
            or \
            (set_vid and hex(d["vendor_id"]).lower() == set_vid.lower())
        ) \
        and \
        (
            (not set_pid) \
            or \
            (set_pid and hex(d["product_id"]).lower() == set_pid.lower())
        )
    for d in dicts:
        if device_filter(d):
            yield(d)

def load_model(model):
    try:
        m = importlib.import_module(f"map_{model}")
    except ImportError as e:
        raise
    return m

def print_default_key_mappings(model):
    m = load_model(model)
    codes = usb_hid_keys.CODES
    i = 0
    print("Direction: Columns left -> right, Keys bottum -> top")
    for column in m.DEFAULT_KEYMAP:
        print(f"---- Column {i:02}")
        i += 1
        j = 0
        for key in column:
            # FIXME Also print modifier key
            name = codes.get(key[-1], "-Unknown Key-")
            print(f"  key {j:02}: {name}")
            j += 1

def send_key_mappings(device, model, data):
    send_data = []
    for column in data:
        for key in column:
            send_data += key
    # Write to device
    print("Writing key mapping to keyboard...")
    
    h = hid.device()
    h.open_path(device["path"])
    h.set_nonblocking(1)

    # Send feature report
    if(VERBOSE):
        print(f"Sending feature report to {device['path']}:")
        print(" ".join([hex(b)[2:] for b in model.KEYDEFINE_FEATURE_REPORT]))
    h.send_feature_report(model.KEYDEFINE_FEATURE_REPORT)

    for i in range(0, len(send_data), model.MESSAGE_LENGTH):
        msg = send_data[i:i+model.MESSAGE_LENGTH] + [0]
        l = len(msg)
        if(VERBOSE):
            print(f"Writing {l} ({hex(l)}) bytes to {device['path']}:")
            text = ""
            i = 0
            for b in msg:
                text += f"{b:02x} "
                i += 1
                if i > 0 and i % 16 == 0:
                    text += "\n"
            print(text)
        time.sleep(0.05)
        h.write(msg)

    print("Done. Closing device...")
    h.close()

    return 0

def set_key_mappings(model, mapping):
    model = load_model(model)
    keys = usb_hid_keys.KEYS
    codes = usb_hid_keys.CODES

    # Parse keys
    changes = {}
    if mapping:
        for k in mapping.split(","):
            pos, name = k.split("=")
            col, row = pos.split(":")
            col, row = int(col), int(row)
            if (col < 0 or col > len(model.DEFAULT_KEYMAP)) or \
                (row < 0 or row > len(model.DEFAULT_KEYMAP[col])):
                raise ValueError(f"Error: Unable to find key {col}, {row} in default key map, please print the default key map and check again")
            if name not in keys:
                raise ValueError(f"Error: Unable to find key name {name}, please check usb_hid_keys.py")
            changes[(col, row)] = keys[name]
    print(f"You have {len(changes)} change(s):")

    # Filter devices with vendor_id, product_id and interface_number
    ids = (hex(model.VENDOR_ID), hex(model.PRODUCT_ID))
    device = None
    for device_dict in filter_device_dicts(hid.enumerate(), ids):
        if device_dict["interface_number"] == model.INTERFACE_NUMBER:
            device = device_dict
            break
    
    data = copy.deepcopy(model.DEFAULT_KEYMAP)
    for pos, code in changes.items():
        col, row = pos
        # FIXME Add modifier support
        data[col][row] = [0x00, 0x00, 0x00, code]
        new_code = [hex(b) for b in data[col][row]]
        old_code = [hex(b) for b in model.DEFAULT_KEYMAP[col][row]]
        print(f"Changing {col} {row}: {old_code} --> {new_code}")
    
    print()
    print("For this device:")
    print_device_dict(device)

    if user_confirm():
        ret = send_key_mappings(device, model, data)
        return ret
    else:
        print("Abort!")
        return 0

def user_confirm():
    QUESTION = "OK to proceed? Y or [N]: "
    sys.stdout.write(QUESTION)
    answer = input()
    if answer.upper() == "Y":
        return True
    return False

def main(args):
    if args.list:
        ids = (None, None)
        if args.print:
            print("Ignoring 'print' arg")
        if args.keys:
            print("Ignoring set keys when listing devices")
        
        if args.id:
            print(f"Filtering with given IDs: {args.id}")
            if args.id.count(",") != 1:
                raise ValueError(f"'id' needs to have exact one ','")
            ids = args.id.split(",")

        if args.model:
            print(f"Filtering with given model: {args.model}")
            m = load_model(args.model)
            ids = (hex(m.VENDOR_ID), hex(m.PRODUCT_ID))
        list_devices(ids)
        return

    if args.print:
        if not args.model:
            print("Error: Cannot print default key mappings without specifying a model")
            return 1
        print_default_key_mappings(args.model)
        return

    if args.keys or args.default:
        if not args.model:
            print("Error: Cannot set key mappings without specifying a model")
            return 1
        keys = None
        if args.keys:
            keys = args.keys
        elif args.default:
            keys = None
        else:
            print("Error: Need to set either keys or default")
            return 1
        ret = set_key_mappings(args.model, keys)
        return ret

if __name__ == "__main__":
    args = argparse.ArgumentParser(description="Varmilo Keyboard Controller in Python")
    args.add_argument("-v", "--verbose", action="store_true", help="Enable verbose output")
    args.add_argument("-l", "--list", action="store_true", help="List all connected devices")
    args.add_argument("-p", "--print", action="store_true", help="Print default key map, needs model")
    args.add_argument("-m", "--model", type=str, help="Set the model of the keyboard")
    # args.add_argument("-c", "--color", type=str, help="Set the color of the keyboard")
    args.add_argument("-i", "--id", type=str, help="Set vendor_id and product_id, e.g. '0x534C,0x0001'")
    args.add_argument("-k", "--keys", type=str, help="Set key mappings to replace 'column:key=NEW_KEY_CODE', e.g. 1:0=LEFTALT,2:0=LEFTMETA,1:1=X")
    args.add_argument("-d", "--default", action="store_true", help="Restore default key mapping")

    args = args.parse_args()

    if args.verbose:
        VERBOSE = True

    main(args)
