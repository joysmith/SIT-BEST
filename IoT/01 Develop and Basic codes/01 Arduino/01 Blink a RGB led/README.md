### Blink a RGB LED

```js
//Prepared by lobiT Solutions
/*Copyrights reserved by lobit Solutions*/

#define LED1RED 5
#define LED1BLUE 3
#define LED1GREEN 4

void setup() {
  // put your setup code here, to run once:
  pinMode(LED1RED, OUTPUT);
  pinMode(LED1BLUE, OUTPUT);
  pinMode(LED1GREEN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED1RED, HIGH);
  Serial.print("LED1RED");
  delay(1000);
  digitalWrite(LED1RED, LOW);
  Serial.print("LED1RED");
  delay(1000);

  digitalWrite(LED1BLUE, HIGH);
  Serial.print("LED1BLUE");
  delay(1000);
  digitalWrite(LED1BLUE, LOW);
  Serial.print("LED1BLUE");
  delay(1000);

  digitalWrite(LED1GREEN, HIGH);
  Serial.print("LED1GREEN");
  delay(1000);
  digitalWrite(LED1GREEN, LOW);
  Serial.print("LED1GREEN");
  delay(1000);
}
```

LED Uno ESP32 STM32
R D5 GPI025 PC13
G D4 GPI026 PC 14
8 D3 GPI027 PC15
