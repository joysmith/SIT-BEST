### Experiencing to interface MPU6050 Sensor and send data to Blynk Cloud App

```js
// library install: Blynk by Volodmyr Shymanskyy
// the compiler will thorw error unless you wont provide credential
#define BLYNK_TEMPLATE_ID "EnterBlynkID"
#define BLYNK_DEVICE_NAME "ESP32 MPU6050"
#define BLYNK_AUTH_TOKEN "EnterAuth Token"


/*
MY BLYNK "JOY" account credential just for testing
#define BLYNK_TEMPLATE_ID "TMPL3CBvWBZSz"
#define BLYNK_TEMPLATE_NAME "NodeMCUBlynk"
#define BLYNK_AUTH_TOKEN "VRBGPRkwFvqr-5Y1HK0RDGXup5rdGUEh"
*/


#define BLYNK_PRINT Serial

#include<WiFi.h>
#include<WiFiClient.h>
#include<BlynkSimpleEsp32.h>

#include<Adafruit_MPU6050.h>
#include<Adafruit_sensor.h>
#include<Wire.h>

char auth[] = BLYNK_AUTH_TOKEN;
char ssid[] = "Enter WiFi SSID"; // Enter your wifi username
char pass[] = "Enter WiFiPass"; // Enter your wifi password

Adafruit_MPU6050 mpu;
BlynkTimer timer;

void setup() {
  Serial.begin(9600);
  while(!Serial){
    delay(10);  // will pause Zero, Leonardo, etc until serial console open
  }

  Serial.println("Adafruit MPU6050 test");

    // Try to initialize!
  if(!mpu.begin()){
    Serial.println("Failed to find MPU6050 chip");
    while(1){
      delay(10);
    }
  }

  Serial.print("MPU6050 Found!");
  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  Serial.print("Acclerometer range set to: ");

  switch(mpu.getAccelerometerRange()){
    case MPU6050_RANGE_2_G:
      Serial.println("+-2G");
      break;

    case MPU6050_RANGE_4_G:
      Serial.println("+-4G");
      break;

    case MPU6050_RANGE_8_G:
      Serial.println("+-8G");
      break;

    case MPU6050_RANGE_16_G:
      Serial.println("+-16G");
      break;
  }

  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  Serial.print("Gyro range set to: ");

  switch(mpu.getGyroRange()){
    case MPU6050_RANGE_250_DEG:
      Serial.println("+-250 deg/s");
      break;

    case MPU6050_RANGE_500_DEG:
      Serial.println("+-500 deg/s");
      break;

    case MPU6050_RANGE_1000_DEG:
      Serial.println("+-1000 deg/s");
      break;

    case MPU6050_RANGE_2000_DEG:
      Serial.println("+-2000 deg/s");
      break;
  }

  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  Serial.print("Filter bandwidth set to: ");

  switch(mpu.getFilterBandwidth()){
    case MPU6050_BAND_260_HZ:
      Serial.println("260 Hz");
    break;

  case MPU6050_BAND_184_HZ:
      Serial.println("184 Hz");
    break;

  case MPU6050_BAND_94_HZ:
      Serial.println("94 Hz");
    break;

  case MPU6050_BAND_44_HZ:
      Serial.println("44 Hz");
    break;

  case MPU6050_BAND_21_HZ:
      Serial.println("21 Hz");
    break;

  case MPU6050_BAND_10_HZ:
      Serial.println("10 Hz");
    break;

  case MPU6050_BAND_5_HZ:
      Serial.println("5 Hz");
    break;
  }

  Serial.println("");
  delay(100);
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(2500L, sendSensor);
}

void loop() {
  // put your main code here, to run repeatedly:
  Blynk.run();
  timer.run();
}

void sendSensor(){
  /* Get new sensor events with the readings */
  sensors_event_t a, g, temp;

  mpu.getEvent(&a, &g, &temp);

  /* print out the values */
  Serial.print("Acclerometer X: ");
  float xx = a.acceleration.x;
  Serial.print(a.acceleration.x);

  Serial.print(",Y: ");
  float yy = a.acceleration.y;
  Serial.print(a.acceleration.y);

  Serial.print(",Z");
  float zz = a.acceleration.z;
  Serial.print(a.acceleration.z);

  Serial.println("m/s^2");
  Serial.println("");

  Blynk.virtualWrite(V2, xx);
  Blynk.virtualWrite(V3, yy);
  Blynk.virtualWrite(V4, zz);
  delay(500);
}
```
