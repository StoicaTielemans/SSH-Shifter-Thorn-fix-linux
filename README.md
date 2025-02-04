So basically, the problem is that the shifter is set up as a non-standard controller, and games (at least the ones I tried) couldn’t detect it.

~~To fix this, I used [AntiMicroX](https://github.com/AntiMicroX/antimicrox) to remap all the controller inputs to keyboard inputs. I mapped the inputs to the numpad keys (1 to 9).~~

**antimicrox died on me**

**So I now made a Python script with uinput and evdev that just rebind all my joystick events to numpad numbers.**

**Just install python-evdev and python-uinput and copy the python script shifter_uinput.py.**

**Run the script like `python3 shifter_uinput.py`**

In the games, you just need to assign the gears to the corresponding numpad numbers, and it should work.

I couldn’t find a solution online for this, so I tried experimenting on my own, and this seems to work for now. I hope it helps! :)

Additionally, to check if your shifter is detected by Linux, you can use tools like `evtest` or `jstest`.
