# pyvarmilo

**pyvarmilo** is a python library to configure Varmilo keyboards. It uses the [hidapi python library](https://pypi.org/project/hidapi/). See the [hidapi C library](https://github.com/libusb/hidapi), too.

# Requirements
Run this first:
```
pip install hidapi
```
Also see install steps [here](https://pypi.org/project/hidapi/#toc-entry-4).

# Supported models
* VDG87 (Tested only on VDG87TTJ)
* VDG104 (NOT tested but should work)
* Other models supported by Varmilo Keyboard [programming firmware](https://cn.varmilo.com/keyboardproscenium/upload/Varmilo-Keyboard.rar) (VDG104/87自定义键值、灯效软件)


# Examples

List all USB keyboards and filter with `vendor_id` or `product_id`
```
python main.py -l
python main.py -l -i 0x4d9,
python main.py -l -i ,0x8008
python main.py -l -m vdg87ttj
```

Print default key map
```
python main.py -p -m vdg87ttj
```

Set key map to default
```
python main.py -v -d -m vdg87ttj
```

Swap LEFTALT and LEFTMETA, RIGHTALT and RIGHTMETA
```
python main.py -v -m vdg87ttj -k 1:0=LEFTALT,2:0=LEFTMETA,9:0=RIGHTMETA,10:0=RIGHTALT
```

# How to contribute

* Implement modifier support
* Search for `FIXME` and work on these
* Feel free to send pull requests

# Development

## Is my keyboard supported?

* Download Varmilo Keyboard [programming firmware](https://cn.varmilo.com/keyboardproscenium/upload/Varmilo-Keyboard.rar) (VDG104/87自定义键值、灯效软件)
* Install and open `Varmilo-Keyboard.exe`. If it shows a green light icon and "ON" at the bottom right of the window, then your keyboard is supported.
* If your keyboard is not supported, you can still send data to it at your own risk. Because you may **brick** it.

## Capture HID data for your keyboard

I suspect that the key mapping are the same across all keyboard models, if the firmware comes with the remapping functionality. But I still recommend you to capture the HID data.

1. Install Visual Studio and Windows SDK
2. Checkout the [hidapi C library](https://github.com/libusb/hidapi)
3. Apply the patch `misc\hidapi.patch`
4. Open `windows\hidapi.sln` and build
5. Copy the `windows\Debug\hdiapi.dll` to `C:\Program Files (x86)\VarmiloKeyboard\`
6. Open `Varmilo-Keyboard.exe`, then click on "KEY" -> check "GAMING MODE".
7. Click on a key and map it to something else, click on the "tick" to confirm. Now the software should send data to your keyboard using `hidapi.dll`.
8. Then restore the default by clicking the "refresh" button right next to the "tick" and then click tick. The software does not work well, but it does not matter.
9. Quit the software by clicking on the top right corner button
10. Open `testlog.txt` and find the feature report data and key mapping data the software sends

The key mapping data structure is straight-forward. It goes by columns from left to right, and keys from bottom to top. Each key code takes 4 bytes and the last byte is the USB HID key code. Read `map_vdg87tti.py` for details.

## Create map for new model

Once you capture the data for your own model, create your `map_MODEL.py` following the example of `map_vdg87tti.py`.