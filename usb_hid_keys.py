# https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
# USB HID Keyboard scan codes as per USB spec 1.11
# plus some additional codes
# 
# Created by MightyPork, 2016
# Public domain
# 
# Adapted from:
# https://source.android.com/devices/input/keyboard-devices.html

# Modifier masks - used for the first byte in the HID report.
# NOTE: The second byte in the report is reserved, 0x00
KEYS = {} 
CODES = None

KEYS["MOD_LCTRL"]   = 0x01
KEYS["MOD_LSHIFT"]  = 0x02
KEYS["MOD_LALT"]    = 0x04
KEYS["MOD_LMETA"]   = 0x08
KEYS["MOD_RCTRL"]   = 0x10
KEYS["MOD_RSHIFT"]  = 0x20
KEYS["MOD_RALT"]    = 0x40
KEYS["MOD_RMETA"]   = 0x80

# Scan codes - last N slots in the HID report (usually 6).
# 0x00 if no key pressed.
# 
# If more than N keys are pressed, the HID reports 
# KEYS["ERR_OVF in all slots to indicate this condition.

KEYS["NONE"]        = 0x00 # No key pressed
KEYS["ERR_OVF"]     = 0x01 #  Keyboard Error Roll Over - used for all slots if too many keys are pressed ("Phantom key")
# 0x02 #  Keyboard POST Fail
# 0x03 #  Keyboard Error Undefined

KEYS["A"] = 0x04 # Keyboard a and A
KEYS["B"] = 0x05 # Keyboard b and B
KEYS["C"] = 0x06 # Keyboard c and C
KEYS["D"] = 0x07 # Keyboard d and D
KEYS["E"] = 0x08 # Keyboard e and E
KEYS["F"] = 0x09 # Keyboard f and F
KEYS["G"] = 0x0a # Keyboard g and G
KEYS["H"] = 0x0b # Keyboard h and H
KEYS["I"] = 0x0c # Keyboard i and I
KEYS["J"] = 0x0d # Keyboard j and J
KEYS["K"] = 0x0e # Keyboard k and K
KEYS["L"] = 0x0f # Keyboard l and L
KEYS["M"] = 0x10 # Keyboard m and M
KEYS["N"] = 0x11 # Keyboard n and N
KEYS["O"] = 0x12 # Keyboard o and O
KEYS["P"] = 0x13 # Keyboard p and P
KEYS["Q"] = 0x14 # Keyboard q and Q
KEYS["R"] = 0x15 # Keyboard r and R
KEYS["S"] = 0x16 # Keyboard s and S
KEYS["T"] = 0x17 # Keyboard t and T
KEYS["U"] = 0x18 # Keyboard u and U
KEYS["V"] = 0x19 # Keyboard v and V
KEYS["W"] = 0x1a # Keyboard w and W
KEYS["X"] = 0x1b # Keyboard x and X
KEYS["Y"] = 0x1c # Keyboard y and Y
KEYS["Z"] = 0x1d # Keyboard z and Z

KEYS["1"] = 0x1e # Keyboard 1 and !
KEYS["2"] = 0x1f # Keyboard 2 and @
KEYS["3"] = 0x20 # Keyboard 3 and #
KEYS["4"] = 0x21 # Keyboard 4 and $
KEYS["5"] = 0x22 # Keyboard 5 and %
KEYS["6"] = 0x23 # Keyboard 6 and ^
KEYS["7"] = 0x24 # Keyboard 7 and &
KEYS["8"] = 0x25 # Keyboard 8 and *
KEYS["9"] = 0x26 # Keyboard 9 and (
KEYS["0"] = 0x27 # Keyboard 0 and )

KEYS["ENTER"]      =  0x28 # Keyboard Return (ENTER)
KEYS["ESC"]        =  0x29 # Keyboard ESCAPE
KEYS["BACKSPACE"]  =  0x2a # Keyboard DELETE (Backspace)
KEYS["TAB"]        =  0x2b # Keyboard Tab
KEYS["SPACE"]      =  0x2c # Keyboard Spacebar
KEYS["MINUS"]      =  0x2d # Keyboard - and _
KEYS["EQUAL"]      =  0x2e # Keyboard = and +
KEYS["LEFTBRACE"]  =  0x2f # Keyboard [ and {
KEYS["RIGHTBRACE"] =  0x30 # Keyboard ] and }
KEYS["BACKSLASH"]  =  0x31 # Keyboard \ and |
KEYS["HASHTILDE"]  =  0x32 # Keyboard Non-US # and ~
KEYS["SEMICOLON"]  =  0x33 # Keyboard ; and :
KEYS["APOSTROPHE"] =  0x34 # Keyboard ' and "
KEYS["GRAVE"]      =  0x35 # Keyboard ` and ~
KEYS["COMMA"]      =  0x36 # Keyboard , and <
KEYS["DOT"]        =  0x37 # Keyboard . and >
KEYS["SLASH"]      =  0x38 # Keyboard / and ?
KEYS["CAPSLOCK"]   =  0x39 # Keyboard Caps Lock

KEYS["F1"]  =  0x3a # Keyboard F1
KEYS["F2"]  =  0x3b # Keyboard F2
KEYS["F3"]  =  0x3c # Keyboard F3
KEYS["F4"]  =  0x3d # Keyboard F4
KEYS["F5"]  =  0x3e # Keyboard F5
KEYS["F6"]  =  0x3f # Keyboard F6
KEYS["F7"]  =  0x40 # Keyboard F7
KEYS["F8"]  =  0x41 # Keyboard F8
KEYS["F9"]  =  0x42 # Keyboard F9
KEYS["F10"] =  0x43 # Keyboard F10
KEYS["F11"] =  0x44 # Keyboard F11
KEYS["F12"] =  0x45 # Keyboard F12

KEYS["SYSRQ"]      =  0x46 # Keyboard Print Screen
KEYS["SCROLLLOCK"] =  0x47 # Keyboard Scroll Lock
KEYS["PAUSE"]      =  0x48 # Keyboard Pause
KEYS["INSERT"]     =  0x49 # Keyboard Insert
KEYS["HOME"]       =  0x4a # Keyboard Home
KEYS["PAGEUP"]     =  0x4b # Keyboard Page Up
KEYS["DELETE"]     =  0x4c # Keyboard Delete Forward
KEYS["END"]        =  0x4d # Keyboard End
KEYS["PAGEDOWN"]   =  0x4e # Keyboard Page Down
KEYS["RIGHT"]      =  0x4f # Keyboard Right Arrow
KEYS["LEFT"]       =  0x50 # Keyboard Left Arrow
KEYS["DOWN"]       =  0x51 # Keyboard Down Arrow
KEYS["UP"]         =  0x52 # Keyboard Up Arrow

KEYS["NUMLOCK"]    =  0x53 # Keyboard Num Lock and Clear
KEYS["KPSLASH"]    =  0x54 # Keypad /
KEYS["KPASTERISK"] =  0x55 # Keypad *
KEYS["KPMINUS"]    =  0x56 # Keypad -
KEYS["KPPLUS"]     =  0x57 # Keypad +
KEYS["KPENTER"]    =  0x58 # Keypad ENTER
KEYS["KP1"]        =  0x59 # Keypad 1 and End
KEYS["KP2"]        =  0x5a # Keypad 2 and Down Arrow
KEYS["KP3"]        =  0x5b # Keypad 3 and PageDn
KEYS["KP4"]        =  0x5c # Keypad 4 and Left Arrow
KEYS["KP5"]        =  0x5d # Keypad 5
KEYS["KP6"]        =  0x5e # Keypad 6 and Right Arrow
KEYS["KP7"]        =  0x5f # Keypad 7 and Home
KEYS["KP8"]        =  0x60 # Keypad 8 and Up Arrow
KEYS["KP9"]        =  0x61 # Keypad 9 and Page Up
KEYS["KP0"]        =  0x62 # Keypad 0 and Insert
KEYS["KPDOT"]      =  0x63 # Keypad . and Delete

KEYS["102ND"]      =  0x64 # Keyboard Non-US \ and |
KEYS["COMPOSE"]    =  0x65 # Keyboard Application
KEYS["POWER"]      =  0x66 # Keyboard Power
KEYS["KPEQUAL"]    =  0x67 # Keypad =

KEYS["F13"] =  0x68 # Keyboard F13
KEYS["F14"] =  0x69 # Keyboard F14
KEYS["F15"] =  0x6a # Keyboard F15
KEYS["F16"] =  0x6b # Keyboard F16
KEYS["F17"] =  0x6c # Keyboard F17
KEYS["F18"] =  0x6d # Keyboard F18
KEYS["F19"] =  0x6e # Keyboard F19
KEYS["F20"] =  0x6f # Keyboard F20
KEYS["F21"] =  0x70 # Keyboard F21
KEYS["F22"] =  0x71 # Keyboard F22
KEYS["F23"] =  0x72 # Keyboard F23
KEYS["F24"] =  0x73 # Keyboard F24

KEYS["OPEN"]       =  0x74 # Keyboard Execute
KEYS["HELP"]       =  0x75 # Keyboard Help
KEYS["PROPS"]      =  0x76 # Keyboard Menu
KEYS["FRONT"]      =  0x77 # Keyboard Select
KEYS["STOP"]       =  0x78 # Keyboard Stop
KEYS["AGAIN"]      =  0x79 # Keyboard Again
KEYS["UNDO"]       =  0x7a # Keyboard Undo
KEYS["CUT"]        =  0x7b # Keyboard Cut
KEYS["COPY"]       =  0x7c # Keyboard Copy
KEYS["PASTE"]      =  0x7d # Keyboard Paste
KEYS["FIND"]       =  0x7e # Keyboard Find
KEYS["MUTE"]       =  0x7f # Keyboard Mute
KEYS["VOLUMEUP"]   =  0x80 # Keyboard Volume Up
KEYS["VOLUMEDOWN"] =  0x81 # Keyboard Volume Down

KEYS["LOCKING_CAPSLOCK"]   =  0x82 # Keyboard Locking Caps Lock
KEYS["LOCKING_NUMLOCK"]    =  0x83 # Keyboard Locking Num Lock
KEYS["LOCKING_SCROLLLOCK"] =  0x84 # Keyboard Locking Scroll Lock

KEYS["KPCOMMA"] =  0x85 # Keypad Comma
# 0x86  Keypad Equal Sign
KEYS["RO"] =  0x87 # Keyboard International1
KEYS["KATAKANAHIRAGANA"] =  0x88 # Keyboard International2
KEYS["YEN"]       =  0x89 # Keyboard International3
KEYS["HENKAN"]    =  0x8a # Keyboard International4
KEYS["MUHENKAN"]  =  0x8b # Keyboard International5
KEYS["KPJPCOMMA"] =  0x8c # Keyboard International6
# 0x8d  Keyboard International7
# 0x8e  Keyboard International8
# 0x8f  Keyboard International9
KEYS["HANGEUL"]  =  0x90 # Keyboard LANG1
KEYS["HANJA"]    =  0x91 # Keyboard LANG2
KEYS["KATAKANA"] =  0x92 # Keyboard LANG3
KEYS["HIRAGANA"] =  0x93 # Keyboard LANG4
KEYS["ZENKAKUHANKAKU"] =  0x94 # Keyboard LANG5
# 0x95  Keyboard LANG6
# 0x96  Keyboard LANG7
# 0x97  Keyboard LANG8
# 0x98  Keyboard LANG9
# 0x99  Keyboard Alternate Erase
# 0x9a  Keyboard SysReq/Attention
# 0x9b  Keyboard Cancel
# 0x9c  Keyboard Clear
# 0x9d  Keyboard Prior
# 0x9e  Keyboard Return
# 0x9f  Keyboard Separator
# 0xa0  Keyboard Out
# 0xa1  Keyboard Oper
# 0xa2  Keyboard Clear/Again
# 0xa3  Keyboard CrSel/Props
# 0xa4  Keyboard ExSel

# 0xb0  Keypad 00
# 0xb1  Keypad 000
# 0xb2  Thousands Separator
# 0xb3  Decimal Separator
# 0xb4  Currency Unit
# 0xb5  Currency Sub-unit
KEYS["KPLEFTPAREN"]  =  0xb6 # Keypad (
KEYS["KPRIGHTPAREN"] =  0xb7 # Keypad )
# 0xb8  Keypad {
# 0xb9  Keypad }
# 0xba  Keypad Tab
# 0xbb  Keypad Backspace
# 0xbc  Keypad A
# 0xbd  Keypad B
# 0xbe  Keypad C
# 0xbf  Keypad D
# 0xc0  Keypad E
# 0xc1  Keypad F
# 0xc2  Keypad XOR
# 0xc3  Keypad ^
# 0xc4  Keypad %
# 0xc5  Keypad <
# 0xc6  Keypad >
# 0xc7  Keypad &
# 0xc8  Keypad &&
# 0xc9  Keypad |
# 0xca  Keypad ||
# 0xcb  Keypad :
# 0xcc  Keypad #
# 0xcd  Keypad Space
# 0xce  Keypad @
# 0xcf  Keypad !
# 0xd0  Keypad Memory Store
# 0xd1  Keypad Memory Recall
# 0xd2  Keypad Memory Clear
# 0xd3  Keypad Memory Add
# 0xd4  Keypad Memory Subtract
# 0xd5  Keypad Memory Multiply
# 0xd6  Keypad Memory Divide
# 0xd7  Keypad +/-
# 0xd8  Keypad Clear
# 0xd9  Keypad Clear Entry
# 0xda  Keypad Binary
# 0xdb  Keypad Octal
# 0xdc  Keypad Decimal
# 0xdd  Keypad Hexadecimal

KEYS["LEFTCTRL"] =  0xe0 # Keyboard Left Control
KEYS["LEFTSHIFT"] =  0xe1 # Keyboard Left Shift
KEYS["LEFTALT"] =  0xe2 # Keyboard Left Alt
KEYS["LEFTMETA"] =  0xe3 # Keyboard Left GUI
KEYS["RIGHTCTRL"] =  0xe4 # Keyboard Right Control
KEYS["RIGHTSHIFT"] =  0xe5 # Keyboard Right Shift
KEYS["RIGHTALT"] =  0xe6 # Keyboard Right Alt
KEYS["RIGHTMETA"] =  0xe7 # Keyboard Right GUI

KEYS["MEDIA_PLAYPAUSE"]    =  0xe8
KEYS["MEDIA_STOPCD"]       =  0xe9
KEYS["MEDIA_PREVIOUSSONG"] =  0xea
KEYS["MEDIA_NEXTSONG"]     = 0xeb
KEYS["MEDIA_EJECTCD"]      =  0xec
KEYS["MEDIA_VOLUMEUP"]     =  0xed
KEYS["MEDIA_VOLUMEDOWN"]   =  0xee
KEYS["MEDIA_MUTE"]         =  0xef
KEYS["MEDIA_WWW"]          =  0xf0
KEYS["MEDIA_BACK"]         =  0xf1
KEYS["MEDIA_FORWARD"]      =  0xf2
KEYS["MEDIA_STOP"]         =  0xf3
KEYS["MEDIA_FIND"]         =  0xf4
KEYS["MEDIA_SCROLLUP"]     =  0xf5
KEYS["MEDIA_SCROLLDOWN"]   =  0xf6
KEYS["MEDIA_EDIT"]         =  0xf7
KEYS["MEDIA_SLEEP"]        =  0xf8
KEYS["MEDIA_COFFEE"]       =  0xf9
KEYS["MEDIA_REFRESH"]      =  0xfa
KEYS["MEDIA_CALC"]         =  0xfb

CODES = {v: k for k, v in KEYS.items()}