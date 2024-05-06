#include "DHT.h"

const int fanPin1 = 9;    // Pin for fan 1
const int fanPin2 = 10;   // Pin for fan 2
const int peltierPin = 11;  // Pin for Peltier
#define DHTPIN 4           // Pin connected to DHT11
#define DHTTYPE DHT11      // DHT 11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  pinMode(fanPin1, OUTPUT);
  pinMode(fanPin2, OUTPUT);
  pinMode(peltierPin, OUTPUT);
  dht.begin();
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'A') {
      digitalWrite(fanPin1, HIGH);
      digitalWrite(fanPin2, HIGH);
      digitalWrite(peltierPin, HIGH);
      Serial.println("Fans ON for Apple");
    } else if (command == 'T') {
      digitalWrite(fanPin1, HIGH);
      digitalWrite(fanPin2, HIGH);
      digitalWrite(peltierPin, HIGH);
      Serial.println("Fans OFF for Tomato");
    }
  }

  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);

  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.println(" %");
  Serial.print("Temperature: ");
  Serial.print(t);
  Serial.println(" *C");
  Serial.print("Fahrenheit: ");
  Serial.print(f);
  Serial.println(" *F");

  // Send sensor data to NodeMCU
  Serial.print("H:");
  Serial.print(h);
  Serial.print(",T:");
  Serial.print(t);
  Serial.print(",F:");
  Serial.println(f);
}
