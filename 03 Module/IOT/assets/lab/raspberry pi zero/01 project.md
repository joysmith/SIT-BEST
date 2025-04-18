### Blink a RGB LED

```js
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
  Serial.println("LED1RED ");
  delay(1000);

  digitalWrite(LED1RED, LOW);
  Serial.println("LED1RED");
  delay(1000);

  digitalWrite(LED1BLUE, HIGH);
  Serial.println("LED1BLUE");
  delay(1000);

  digitalWrite(LED1BLUE, LOW);
  Serial.println("LED1BLUE");
  delay(1000);

  digitalWrite(LED1GREEN, HIGH);
  Serial.println("LED1GREEN");
  delay(1000);

  digitalWrite(LED1GREEN, LOW);
  Serial.println("LED1GREEN");
  delay(1000);
}
```
