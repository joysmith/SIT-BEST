### Interfacing BMP280 Sensor

🔴 code need correction may be library fault

```js
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_BME280.h>


#define BME_SCK 13
#define BME_MISO 12
#define BME_MOSI 11
#define BME_CS 10


Adafruit_BME280 bme; // I2C by default for comm.
// Adafruit_BME280 bme(BME_CS); // hardware SPI
// Adafruit_BME280 bme(BME_CS, BME_MOSI, BME_MISO,  BME_SCK);

void setup() {
  Serial.begin(9600);

  while(!Serial) delay(100); // wait for native usb

  Serial.println(F("BME280 test"));
  Unsigned status;
  // status = bmp.begin(BMP280_ADDRESS_ALT, BMP280_CHIPID);
  status = bmp.begin(0x76);
  if(!status){
    serial.println(F("Could not find a valid BMP280 sensor, check wiring or try a different address!"))
    Serial.println("SensorID was:0x");
    Serial.println(bmp.sensorID(), 16);
    Serial.println("ID of 0xff probably means a bad address, a BMP 180 or BMP 085\n");
    Serial.println(" ID of 0x56-0x58 represents a BMP 280,\n ");
    Serial.println("  ID of 0x60 represents a BMP 280,\n  ");
    Serial.println("  ID of 0x60-0x58 represents a BMP 280,\n  ");
    Serial.println(" ID of 0x61 represents a BMP 280,\n ");
    while(1) dealy(10);
  }


  /* Default settings from datasheet */
  bmp.setSampling(adafruit_BMP280::MODE_NOARMAL, /* Operating Mode*/
                  adafruit_BMP280::SAMPLING_X2, /* Temp oversampling */
                  adafruit_BMP280::SAMPLING_X16, /* Pressure oversampling*/
                  adafruit_BMP280::FILTER_X16, /* Filtering*/
                  adafruit_BMP280::STANDBY_MS_500, /* Standby time*/
                  )
}



void loop() {
    Serial.print("Temperature = ");
    Serial.print(bmp.readTemperature());
    Serial.println(" *C");

    Serial.print("Pressure = ");

    Serial.print(bmp.readPressure());
    Serial.println(" Pa");

    Serial.print(F("Approx altitude = "));
    Serial.print(bmp.readAltitude(1013.25); // Adjusted to local forecast
    Serial.println(" m");
    Serial.println();
    delay(2000);
}
```
