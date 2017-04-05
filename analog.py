#!/usr/bin/python
#analog.py

import RPi.GPIO as GPIO, time, os

#my vars
mySecDischarge = 0.5  #
myRCpin = 17

GPIO.setmode(GPIO.BCM)

def RCtime (xRCpin,xSecDischarge):
   #0--reset reading
    reading = 0

   #1--discharging Cap.
    GPIO.setup(xRCpin, GPIO.OUT)
    GPIO.output(xRCpin, GPIO.LOW)
    time.sleep(xSecDischarge)

   #2--charging Cap.
    GPIO.setup(xRCpin, GPIO.IN)

   #3--wait until "0"->"1"    
    while (GPIO.input(xRCpin) == GPIO.LOW):
        reading += 1
    
   #4--done
    return reading

while True:
   # Read RC timing using xpinRC
	print RCtime(myRCpin,mySecDischarge) 
    
