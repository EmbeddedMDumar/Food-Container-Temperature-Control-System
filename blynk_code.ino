#define BLYNK_TEMPLATE_ID "TMPL3Fm42dznl"
#define BLYNK_TEMPLATE_NAME "Ship Container"
#define BLYNK_AUTH_TOKEN "106mDlh8jmutK19YlNiZ-m_RuhHZLXYl"
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "106mDlh8jmutK19YlNiZ-m_RuhHZLXYl";  // Your Blynk Auth Token
char ssid[] = "iotadmin";   // Your WiFi SSID
char pass[] = "12345678"; // Your WiFi Password

#define BLYNK_PRINT Serial
float latitude,longitude;
String lat_str ="12.9576° N";
String lng_str ="80.1599° E";
String loc = lat_str +":"+ lng_str;


void setup() {
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);
}

void loop() {
  Blynk.run();
  if (Serial.available() > 0) {
    String sensorData = Serial.readStringUntil('\n');
    Serial.println(sensorData);

    // Parse sensor data
    int index1 = sensorData.indexOf("H:");
    int index2 = sensorData.indexOf(",T:");
    int index3 = sensorData.indexOf(",F:");

    if (index1 != -1 && index2 != -1 && index3 != -1) {
      String humidityStr = sensorData.substring(index1 + 2, index2);
      String tempStr = sensorData.substring(index2 + 3, index3);
      String fahrStr = sensorData.substring(index3 + 3);

      float humidity = humidityStr.toFloat();
      float temp = tempStr.toFloat();
      float fahr = fahrStr.toFloat();
      Blynk.virtualWrite(V0,temp);
      Blynk.virtualWrite(V1,humidity);
      Blynk.virtualWrite(V2,fahr);
      Blynk.virtualWrite(V3,loc);
    }
  }
}
