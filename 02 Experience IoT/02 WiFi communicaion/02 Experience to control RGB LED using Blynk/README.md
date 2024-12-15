### Experiencing to control RGB LED using Blynk

```js
// library install: Blynk by Volodmyr Shymanskyy
// the compiler will thorw error unless you wont provide credential
#define BLYNK_TEMPLATE_ID "EnterBlynkID"
#define BLYNK_DEVICE_NAME "ESP32 MPU6050"
#define BLYNK_AUTH_TOKEN "EnterAuth Token"



// MY BLYNK "JOY" account credential just for testing
// #define BLYNK_TEMPLATE_ID "TMPL3CBvWBZSz"
// #define BLYNK_TEMPLATE_NAME "NodeMCUBlynk"
// #define BLYNK_AUTH_TOKEN "VRBGPRkwFvqr-5Y1HK0RDGXup5rdGUEh"



#define BLYNK_PRINT Serial

#include<WiFi.h>
#include<WiFiClient.h>
#include<BlynkSimpleEsp32.h>


char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Enter WiFi SSID"; // Enter your wifi username
char pass[] = "Enter WiFiPass"; // Enter your wifi password

int ledpin = 2;
void setup() {
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  pinMode(ledpin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();
}
```
