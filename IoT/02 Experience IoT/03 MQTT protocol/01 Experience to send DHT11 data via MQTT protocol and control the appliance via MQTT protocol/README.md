# Experience to send the DHT11 data via MQTT protocol and control the appliance via MQTT protocol

```js
// Install Library: PubSinClient by Nick O'Leary

#include<Arduino.h>
#include<WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

#define DHTPIN 4     // what pin we're connected to
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "Type your SSID";
const char* password = "your password";

char*mqttServer = "broker.hivemq.com";
int mqttPort = 1883;

void setupMQTT(){
  mqttClient.setServer(mqttServer, mqttPort);
  mqttClient.setCallback(callback);
}

void reconnect(){
  Serial.println("Connecting to MQTT Broker...");
  while(!mqttClient.connected()){
    Serial.println("Reconnecting to MQTT Broker...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xff), HEX);

    if(mqttClient.connect(clientId.c_str())){
      Serial.println("Connected.");

      // subscribe to topic
      mqttClient.subscribe("esp32/message");
    }
  }
}



#define wifi_ssid "xxxxx"
#define wifi_password "xxxxx"

#define mqtt_server "broker-internet-facing-f1429d8cb54ca4a7.elb.us-east-1.amazonaws.com"  // MQTT Cloud address
#define humidity_topic "humidity"
#define temperature_topic "temperature"

void setup() {
    Serial.begin(115200);
    Serial.println("DHT11 test");
    dht.begin();
    WiFi.begin(ssid, password);

    while(WiFi.status() != WL_CONNECTED){
      delay(500);
      Serial.print(".");
    }

    Serial.println(" ");
    Serial.println("Connected to Wi-Fi");
    pinMode(2, OUTPUT);
    setupMQTT();
}


void loop() {
  if(!mqttClient.connected())
  reconnect();
  mqttClient.loop();
  long now = millis();
  long previous_time = 0;

  if(now - previous_time > 1000){
    previous_time = now;

    float h = dht.readHumidity();
    float t = dht.readTemperature();

    if(isnan(h) || isnan(t)){
      Serial.println("Failed to read from DHT sensor");
      return;
    }

    char tempString[8];
    dtostrf(t, 1, 2, tempString);
    Serial.print("Temperature: ");
    Serial.println(tempString);
    mqttClient.publish("esp32/temperature", tempString);

    char humString[8];
    dtostrf(h, 1, 2, humString);
    Serial.print("Humidity: ");
    Serial.println(humString);
    mqttClient.publish("esp32/humidity", humString);
    delay(2000);
  }
}


void callback(char* topic, byte* message, unsigned int length){
  Serial.print("Callback- ");
  Serial.print("Message: ");
  String messageTemp;

  for(int i=0; i<length; i++){
    Serial.print((char) message[i]);
    messageTemp += (char) message[i];
  }

  Serial.println();

  if(String(topic) == "esp32/message"){
    Serial.print("Changing output to ");

    if(messageTemp == "on"){
      Serial.println("on");
      digitalWrite(2, HIGH);
    }else if(messageTemp == "off"){
      Serial.print("off");
      digitalWrite(2, LOW);
    }
  }
}
```
