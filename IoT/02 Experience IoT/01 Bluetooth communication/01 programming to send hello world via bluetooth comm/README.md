### Program to send "Hello world" via bluetooth communication

```js
#include <BluetoothSerial.h>

#if !defined(CONFIG_BT_ENABLED) || !defined(CONFIG_BLUEDROID_ENABLED)
#error Bluetooth is not enabled! Please run `make menuconfig` to and enable it
#endif

BluetoothSerial SerialBT;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("ESP32test"); // Bluetooth device name
  Serial.println("The device started now you can pair it with bluetooth");
}


void loop() {
  if (Serial.available()) {
    SerialBT.write(Serial.read());
  }

  if (SerialBT.available()) {
    Serial.write(SerialBT.read());
  }

  delay(20);
}
```

LED Uno ESP32 STM32
R D5 GPI025 PC13
G D4 GPI026 PC 14
8 D3 GPI027 PC15
