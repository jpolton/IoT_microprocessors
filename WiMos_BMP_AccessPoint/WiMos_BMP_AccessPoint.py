# ESP8266_BMP_AccessPoint.py
#
#########################################################
# THESE HEADER COMMENTS AND CODE ARE COPIED FROM ESP8266_BMP_serial_plot.py
# THEY NEED EDITING.
#########################################################
#
#    FILE: ESP8266_BMP_AccessPoint.py
#  AUTHOR: jpolton
#    DATE: 18 Oct 2016
# PURPOSE: Read streaming data from the WiFi Access Point 192.168.1.4/pressure and plot graphs of temperature and pressure.
#          Data stream created by ESP8266_BMP_AccessPoint.ino
#   BOARD: ESP8266 NodeMCU 1.0 (ESP-12E module)
#FIRMWARE: Arduino IDE
# SENSORS: BMP280
#     URL:
# HISTORY:
# 0.1.00 initial version. Gleaned from library demo. Works.
#
# STATUS: WORKS
#
#   NOTE: Can not have both Arduino IDE and python reading
#         the serial data stream at the same time
#
# WIRING: (note in some places the D3 and D4 pins were reversed, but this doesn't work)
# VCC      Red   3V3
# GND      blk   GND
# SCK,SCL  blue  D3
# SDA,SDI  purp  D4
# CSB
# SDO      brn   3V3
#
# To run launch ipython and type run ESP8266_BMP_serial_plot.py
#$ ipython
#>> run ESP8266_BMP_serial_plot.py
#
# COMMENTS
# * This method produces plots at 30Hz. This is the speed you get with random data ==> rate is not limited by comms but by matplotlib method
# * It would be good to plot both temperature and pressure, as relic code suggests.



import requests
import numpy as np
import matplotlib.pyplot as plt
import time

tempArr = []
pressArr = []
timeArr = []
pressLog = []
timeLog = []

plt.ion() # Tell matplotlib want ot interactive mode to plot data
cnt=0

duration = 10*60  # Duration for sampling (s)
N = 250 # number of data points stored in memory
freq = 20 # Expected download freq (Hz). Sets the x-axis range - Had 15Hz to 30Hz
link = "http://192.168.4.1/pressure"

def running_mean(x, N):
    cumsum = np.cumsum(np.insert(x, 0, 0))
    return (cumsum[N:] - cumsum[:-N]) / N

def readsensor():
    startread = time.time()
    #print 'pre'

    try:
 	       f = requests.get(link)
    except requests.exceptions.ConnectionError:
	       f.status_code = "Connection refused"

#    f = requests.get(link, timeout=1)  # It gets stuck here
    #print 'post', f
    while(len(f.text)==0): # Seem to get empty returns. Avoid this!
         f = requests.get(link, timeout=2)
         print '.'
    dataString = f.text
    press = float(dataString.split(' ')[1])
    #press = float(requests.get(link).text.split(' ')[1])
    #print 'time in readsensor:', time.time() - startread
    return press

#####

tstart = time.time()
while ( cnt <= N ): # Fill up the data array buffer
	press = readsensor()
	pressArr.append(press)                     #Building our pressure array by appending P readings
	timeArr.append(time.time()-tstart)
	print cnt, ': ', press
	cnt=cnt+1
	if(cnt>N):                            #If you have 50 or more points, delete the first one from the array
		pressArr.pop(0)
		timeArr.pop(0)


# Setting the plot up
fig, ax = plt.subplots()
line, = ax.plot(np.linspace(-float(N)/float(freq), 0, N), np.random.randn(N))
ax.lines.remove(line) # remove line from bg
fig.canvas.draw()
line, = ax.plot(range(N), 101020*np.random.randn(N))

plt.pause(1)

# Set up the plot details
dp = np.max([np.max(pressArr) - np.min(pressArr), 10])
plt.ylim( np.min(pressArr)-dp, np.max(pressArr)+dp )
plt.xlim( -float(N)/float(freq), 0 )
plt.xlabel('Time since now (s)')
plt.ylabel('Pressure (Pa)')
plt.grid(True)
line, = ax.plot( timeArr, pressArr,'.' )

cnt = 0

tspinup = time.time() - tstart
while (time.time()-tstart < tspinup + duration): # While loop that loops forever
    press = readsensor()
    pressArr.append(press)                     #Building our pressure array by appending P readings
    timeArr.append(time.time()-tstart)
    cnt=cnt+1
    pressArr.pop(0)
    timeArr.pop(0)
    line.set_xdata([ timeArr[i] - timeArr[-1] for i in range(N)])
    smoothArr = np.insert( np.insert( running_mean(pressArr, 3), \
        -1,pressArr[-1]), 0,pressArr[0])  # 3 point running mean. Pad out end with actual values. Would be better to POP after this.
#	line.set_ydata(pressArr)
    line.set_ydata(smoothArr)
    fig.canvas.draw()
    fig.canvas.flush_events()
    #print [np.shape(pressArr)]
    #print np.size(pressArr), np.size(running_mean(pressArr, 9))

    if (np.mod( int(time.time()-tstart-tspinup) , 60) == 0):
        pressLog.append(press)
        timeLog.append( time.time()-tstart-tspinup)

print 'Freq:',cnt/float(duration),'Hz'

# Add final plot to show summary log data. Exporting data to mySQL database would be better.
fig, ax = plt.subplots()
line, = ax.plot(timeLog, pressLog)
plt.xlabel('Time (s)')
plt.ylabel('Pressure (Pa)')
fig.canvas.draw()
