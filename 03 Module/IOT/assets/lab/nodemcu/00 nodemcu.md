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

7. Press the ESP32 on-board Enable button and you should see the networks available near your ESP32
