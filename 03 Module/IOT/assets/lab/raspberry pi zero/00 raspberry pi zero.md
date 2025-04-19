## Micro controller: Raspberry Pi Pico

### Raspberry Pi Pico uno specification

- Specification [Click me](https://docs.arduino.cc/hardware/uno-rev3/#tech-specs)

<br>

### Where to download Thonny IDE

- Download Thonny IDE [Click me](https://thonny.org/)

<br>

### How to Configure Interpreter

- Open Thonny IDE--> run--> Interpreter--> “MicroPython (Raspberry Pi Pico)"--> ok
- Install MicroPython for Pico: First, hold down the “BOOTSEL" button on Pico; then, while still holding it down, connect Pico to a computer using a USB cable.
- Open INDEX.HTM --> Drop down and click on the MicroPython--> Click on the “Download UF2.file" [direct link click me](https://datasheets.raspberrypi.com/soft/flash_nuke.uf2)
- First, connect Pico to the computer using a USB cable; then, open Thonny, and click on
  the “restart back-end process" button on the toolbar. If you successfully connect Pico to your
  computer, you will see the MicroPython version information and device name returned by Pico in
  the Shell area

<br>

### How to Select sketch

- From menu select file--> example--> digital--> BlinkwithoutDelay

<br>

### The Arduino IDE - Understanding the Preferences pane<a id="55"></a>

<img src="assets/images/1.png" width="700">

<br>

### How to upload a sketch to your Arduino<a id="57"></a>

- go to menu Files--> Example--> basic--> blink
- go to menu Tools--> Boards--> arduino avr board--> arduino uno
- go to menu Tools--> Port--> COM(arduino)

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

- click on ✅ to compile, then ➡️ to upload sketch on uno

<br>

### How to use serial monitor

<img src="assets/images/3.png" width="700">

- go to menu Files--> Example--> basic--> blink
- go to menu Tools--> Boards--> arduino avr board--> arduino uno
- go to menu Tools--> Port--> COM(arduino)

```ino

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  Serial.println("ON");

  digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  delay(1000);                     // wait for a second
  Serial.println("OFF");
}

```

- click on ✅ to compile, then ➡️ to upload sketch on uno
- go to menu Tools--> Serial Monitor

<br>

### How to use Serial Plotter

<img src="assets/images/2.png" width="700">

- go to menu Files--> Example--> basic--> blink
- go to menu Tools--> Boards--> arduino avr board--> arduino uno
- go to menu Tools--> Port--> COM(arduino)

```ino

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second
  Serial.println(10);

  digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  delay(1000);                     // wait for a second
  Serial.println(0);
}

```

- click on ✅ to compile, then ➡️ to upload sketch on uno
- go to menu Tools--> Serial Plotter

<br>

### Documentation

- Serial communication documentation [Click me](https://www.arduino.cc/reference/en/language/functions/communication/serial/read/)

- Language reference documentation [Click me](https://docs.arduino.cc/language-reference/)

<br>
