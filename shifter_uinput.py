import uinput
import evdev

BTN_MAP = {
    288: uinput.KEY_KP1,  # BTN_TRIGGER -> Numpad 1
    289: uinput.KEY_KP2,  # BTN_THUMB -> Numpad 2
    290: uinput.KEY_KP3,  # BTN_THUMB2 -> Numpad 3
    291: uinput.KEY_KP4,  # BTN_TOP -> Numpad 4
    292: uinput.KEY_KP5,  # BTN_TOP2 -> Numpad 5
    293: uinput.KEY_KP6,  # BTN_PINKIE -> Numpad 6
    294: uinput.KEY_KP7,  # BTN_BASE -> Numpad 7
    295: uinput.KEY_KP8,  # BTN_BASE2 -> Numpad 8
    298: uinput.KEY_KP0,  # BTN_BASE3 -> Numpad 9
    299: uinput.KEY_KP9,  # BTN_BASE3 -> Numpad 9
}

device_path = "/dev/input/event16"  
shifter = evdev.InputDevice(device_path)

virtual_device = uinput.Device(BTN_MAP.values())

print(f"Listening for events on {shifter.path}...")

for event in shifter.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.code in BTN_MAP:
        virtual_device.emit(BTN_MAP[event.code], event.value)

