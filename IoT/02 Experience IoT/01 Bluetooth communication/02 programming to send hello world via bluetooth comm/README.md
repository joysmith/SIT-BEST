### Program to switch buzzer via bluetooth communication

```js
#include <BluetoothSerial.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

#define BUZZER 2

BluetoothSerial SerialBT;

// Handle received and sent message
String message = "";
char incomingChar;

void setup() {
  pinMode(BUZZER, OUTPUT);
  Serial.begin(115200);
  SerialBT.begin("ESP32"); // Bluetooth device name
  Serial.println("The device started now you can pair it with bluetooth");
}

void loop() {
  if (Serial.available()) {
    char incomingChar = SerialBT.read();
    if(incomingChar != '\n'){
      message += String(incomingChar);
    }else{
      message = "";
    }

    Serial.write(incomingChar);
  }

  // check received message and control output accordingly
  if (message == "on") {
    digitalWrite(BUZZER, HIGH);
  }else if(message == "off"){
    digitalWrite(BUZZER, LOW);
  }

  delay(20);
}
```
