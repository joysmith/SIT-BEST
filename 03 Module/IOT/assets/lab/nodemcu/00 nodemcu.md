## Micro controller: ESP32

### Setting up ESP32 in the Arduino IDE on Windows

- download arduino ide [click me](https://www.arduino.cc/en/software)

<br>

#### Install the drivers USB chip<a id="13"></a>

- Download and Install Drivers for window[click me](<https://github.com/joysmith/Shri-Shankaracharya-Technical-Campus/blob/main/5%20sem%20DS(A%20%2B%20B)%20%20-IOT/Resource/pololu-cp2102-windows-220616.zip>)
- restart system

<br>

#### How to setup nodemcu(esp8266) board

1. Open arduino, go to file--> preference--> additional board manager URL:_paste json link here_

```sh
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

2. Open arduino, go to tools--> board--> board manger--> search:"ESP32 by EspressifSystems" --> install

3. Open arduino, go to tools--> boards--> "DOIT ESP32 DEVKITV1"

4. go to menu Tools--> Port--> COM(arduino)

5. Paste code to ide to blink builtin led

```js
const int ledPin = 2; // GPIO2 is usually the built-in LED

void setup() {
  pinMode(ledPin, OUTPUT); // Set the pin as an output
}

void loop() {
  digitalWrite(ledPin, HIGH); // Turn the LED on
  delay(1000);              // Wait for 1 second
  digitalWrite(ledPin, LOW);  // Turn the LED off
  delay(1000);              // Wait for 1 second
}
```

6. Press the ESP32 on-board Enable button when on consol appear "Connecting ............"
