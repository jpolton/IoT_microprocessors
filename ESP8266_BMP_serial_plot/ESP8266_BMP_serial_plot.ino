//    FILE: ESP8266_BMP_serial_plot.ino
//  AUTHOR: jpolton
// VERSION: 14.10.16
// PURPOSE: Read BMP280 pressure module on ESP8266. Stream to serial.
//          Plot using python: ESP8266_BMP_serial_plot.py to graph live data
//   BOARD: ESP8266 NodeMCU 1.0 (ESP-12E module)
//FIRMWARE: Arduino IDE
// SENSORS: BMP280
//     URL:
// HISTORY:
// 0.1.00 initial version. Gleaned from library demo. Works.
//
// STATUS: WORKS
//
//   NOTE: Can not have both Arduino IDE and python reading
//         the serial data stream at the same time
//
// WIRING: (note in some places the D3 and D4 pins were reversed, but this doesn't work)
// VCC      Red   3V3
// GND      blk   GND
// SCK,SCL  blue  D3
// SDA,SDI  purp  D4
// CSB
// SDO      brn   3V3

#include <ESP8266WiFi.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BMP280.h>  // import pressure sensor library

Adafruit_BMP280 bmp; // I2C. Create sensor object

void setup() {
  Wire.begin(2,0); // GPIO2, GPIOO -> D4, D3
  //Serial.begin(115200);
  Serial.begin(9600);
  Serial.println(F("BMP280 test"));
  
  if (!bmp.begin()) {  
    Serial.println("Could not find a valid BMP280 sensor, check wiring!");
    while (1);
  }
}

void loop() {
  // Wait a few seconds between measurements.
  delay(15);

  //Serial.print("Temperature = ");
  //Serial.print(bmp.readTemperature());
  //Serial.println(" *C");    
  //Serial.print("Pressure = ");
  //Serial.print(bmp.readPressure());
  //Serial.println(" Pa");
  //Serial.println();

  Serial.print(bmp.readTemperature());
  Serial.print(", ");
  Serial.println(bmp.readPressure());
  
}

