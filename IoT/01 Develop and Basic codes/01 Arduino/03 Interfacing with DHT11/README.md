### Interfacing with DHT11 sensor

```js
#include "DHT.h"
#define DHTPIN 2 // Digital pin connected to the DHT sensor

#define DHTTYPE DHT11 //DHT 11

// initalize DHT sensor
DHT dht(DHTPIN, DHTTYPE);

void setup(){
  Serial.begin(9600);
  Serial.println("DHTxxtest!");
  dht.begin();
}

void loop(){
  delay(2000); //Wait a few seconds between measurements

  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperaute as Celsius(the default)
  float t = dht.readTemperature();

  // Check if any reads failed and exit early (to try again)
  if(isnan(h)||isnan(t)){
    Serial.print("Failed to read from DHT sensor!");
    return;
  }


  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("% Temperature: ");
  Serial.print(t);
  Serial.print("C");
}
```
