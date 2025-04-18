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

4. Open the following example under File > Examples > WiFi (ESP32) > WiFiScan

5. go to menu Tools--> Port--> COM(arduino)

6. Open the Arduino IDE Serial Monitor at a baud rate of 115200

```ino

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  delay(1000);                      // wait for a second

  digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
  delay(1000);                     // wait for a second
}

```

- click on ✅ to compile, then ➡️ to upload sketch on nodemcu

<br>

```ino
#define led D0

void setup()
{
  pinMode(led, OUTPUT);
}

void loop()
{
  digitalWrite(led, HIGH);
  delay(500);
  digitalWrite(led, LOW);
  delay(500);
}

```

#### extra

- reference [click me](<https://github.com/joysmith/Shri-Shankaracharya-Technical-Campus/blob/main/5%20sem%20DS(A%20%2B%20B)%20%20-IOT/Resource/project%203%20-%20nodemcu%20blink.pdf>)
