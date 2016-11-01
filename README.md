===================
IoT_microprocessors
===================

ESP8266 or Arduino (nano) projects to read sensors and stuff.

README.md
=========

* This file.

----

===========================
Pressure streaming projects
===========================

BMP280 streaming pressure through a ESP8266 WiFi Access Point. Also include python scripts to GET and stream realtime data using matplotlib. Note the ESP8266 was stabilised using a voltage regulator (ADD DETAILS). This project was developed and tested on two boards:
ESP8266 NodeMCU 1.0 (ESP-12E module) and WeMos D1 R2. Each had their own .ino and .py file for development purposes and fiddling with soft variables but they are essentially the same. 

WIRING::

  BMP280 WIRING: (note in some web instructions the D3 and D4 pins were reversed, but this doesn't work for me)
  VCC      Red   3V3 <--> VOUT of voltage regulator <-->  2x AA 1.5V batteries in series
  GND      blk   GND <--> GND of voltage regulator  <-->  2x AA 1.5V batteries in series  
  SCK,SCL  blue  D3
  SDA,SDI  purp  D4
  CSB
  SDO      brn   3V3 <--> VOUT of voltage regulator

  Voltage regulator:
  VOUT --> BMP280 VCC & SDO
  VIN  --> 2x AA 1.5V batteries in series
  GND  --> 2x AA 1.5V batteries in series


ESP8266_BMP_serial_plot.py
==========================

 * Read streaming data from the serial port and plot graphs of temperature and pressure.
 * Data stream created by ESP8266_BMP_serial_plot.ino


ESP8266_BMP_AccessPoint/
========================

file: **ESP8266_BMP_AccessPoint.ino**
file : **ESP8266_BMP_AccessPoint.py**

* Create a ESP8266 WiFi Access Point server.
* Read BMP280 pressure module on ESP8266.
* Serve data on AP: e.g.
http://192.168.4.1/temp http://192.168.4.1/pressure
* Read and plot data using python

Could add temperature stream
