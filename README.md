===================
IoT_microprocessors
===================

ESP8266 or Arduino (nano) projects to read sensors and stuff.

README.md
=========

* This file.
Had some issues getting the WiFi stable at work compared to home. Perhaps there is something lurking in the WiFi settings that are satisfied on the home network but not at work... After flashing the devise (google is your friend) the WiFi was stable:

esptool.py -p /dev/tty.wchusbserial1410 erase_flash

----

===========================
Pressure streaming projects
===========================

BMP280 streaming pressure through a ESP8266 WiFi Access Point. Also include python scripts to GET and stream realtime data using matplotlib. Note the ESP8266 was perhaps stabilised using a voltage regulator (3.3V Step-Up Voltage Regulator U1V10F3), but worked fine without. However without the regulator the useful life of the batteries would (probably) be much less. This project was developed and tested on two boards:
ESP8266 NodeMCU 1.0 (ESP-12E module) and WeMos D1 R2. Each had their own .ino and .py file for development purposes and fiddling with soft variables but they are essentially the same.

WIRING::

  BMP280 WIRING: (note in some web instructions the D3 and D4 pins were reversed, but this doesn't work for me)
  VCC      Red   3V3 <--> VOUT of voltage regulator <-->  2x AA 1.5V batteries in series
  GND      blk   GND <--> GND of voltage regulator  <-->  2x AA 1.5V batteries in series  
  SCK,SCL  blue  D3
  SDA,SDI  purp  D4
  CSB
  SDO      brn   3V3 <--> VOUT of voltage regulator

  Voltage regulator (3.3V Step-Up Voltage Regulator U1V10F3. http://www.hobbytronics.co.uk/u1v10f3-3v3-regulator?keyword=U1V10F3):
  VOUT --> BMP280 VCC & SDO
  VIN  --> 2x AA 1.5V batteries in series
  GND  --> 2x AA 1.5V batteries in series


ESP8266_BMP_AccessPoint/
========================

file: **ESP8266_BMP_AccessPoint.ino**

* Create a ESP8266 WiFi Access Point server.
* Read BMP280 pressure module on ESP8266.
* Serve data on AP: e.g.
http://192.168.4.1/temp http://192.168.4.1/pressure

file : **ESP8266_BMP_AccessPoint.py**

* Read and plot data using python: e.g. ipython$ run ESP8266_BMP_AccessPoint.py
* Read streaming data from WiFi access point.
* Plot real time data stream.

Could add temperature stream
