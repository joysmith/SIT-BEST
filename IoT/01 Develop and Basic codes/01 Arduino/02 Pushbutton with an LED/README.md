### Pushbutton with an LED

```js
//Prepared by lobiT Solutions
/*Copyrights reserved by lobit Solutions*/

#define BUTTON_PIN 4
#define LED_PIN 13

// the below are the variables which can be changed
int button_state = 0;

void setup() {
  // Initialize the LED as an output
  pinMode(LED_PIN, OUTPUT);

  // initialize the button pin as an pull-up input
  // the pull-up input pin will be HIGH when the button is open and LOW when the button is pressed
  pinMode(BUTTON_PIN, INPUT);
  Serial.begin(9600);
}

void loop() {
  // read the state of button value
  button_state = digitalRead(BUTTON_PIN);
  Serial.print("BUTTON VALUE");
  Serial.print(button_state);
  delay(100);

  // control LED according to the state of button
  if(button_state == LOW){
    digitalWrite(LED_PIN, HIGH); // turn on LED
  }else{
    digitalWrite(LED_PIN, LOW); // turn off LED
  }

}
```
