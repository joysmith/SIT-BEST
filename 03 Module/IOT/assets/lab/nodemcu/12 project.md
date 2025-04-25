## Experiencing to Control RGB LED using Blynk

```js
//Control LED Using Blynk 2.0/Blynk IOT
#define BLYNK_TEMPLATE_ID "Enter Blyk ID"
#define BLYNK_DEVICE_NAME "LED CONTROL"
#define BLYNK_AUTH_TOKEN "Enter Auth Token"
#define BLYNK_PRINT Serial
#include <WiFi.h>
#include <WiFiClient.h>
#include <BlynkSimpleEsp32.h>

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Type Your SSID"; // Enter your Wifi Username
char pass[] = "Type your Pass"; // Enter your Wifi password
int ledpin = 2;

void setup()
{
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  pinMode(ledpin,OUTPUT);
}

void loop()
{
  Blynk.run();
}
```
