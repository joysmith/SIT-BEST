## Micro controller: Raspberry Pi Pico

### Raspberry Pi Pico specification

- Specification [Click me](https://www.raspberrypi.com/documentation/microcontrollers/pico-series.html)

<br>

### Where to download Thonny IDE

- Download Thonny IDE [Click me](https://thonny.org/)

<br>

### How to Configure Interpreter

1. Open Thonny IDE--> run--> Interpreter--> “MicroPython (Raspberry Pi Pico)"--> ok
2. __Install MicroPython for Pico__: First, hold down the “BOOTSEL" button on Pico; then, while still holding it down, connect Pico to a computer using a USB cable.
3. "New drive will appear" Open INDEX.HTM --> Pico series microcontroller--> Click on the “Download UF2.file" [direct link click me](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)
4. Open Thonny IDE--> run--> Interpreter--> Install or update firmware--> ok
5. Unplug and reconnect Pico to the computer using a USB cable; then, open Thonny, and click on the “restart back-end process" button on the toolbar. If you successfully connect Pico to your computer, you will see the MicroPython version information and device name returned by Pico in the Shell area

<br>

### How to upload a sketch to your Arduino<a id="57"></a>

- Open Thonny IDE and in editor paste builtin blink led code and click on "run" button

```py
import machine
import time

led = machine.Pin(25, machine.Pin.OUT)

while True:
    led.value(True)
    time.sleep(2)
    led.value(False)
    time.sleep(2)

```

- click on "run" button to upload code

<br>

### Documentation


- Language reference documentation [Click me](https://docs.micropython.org/en/latest/rp2/quickref.html)

<br>
