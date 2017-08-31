#!/usr/bin/python

from string import split
import RPi.GPIO as GPIO
from time import sleep

relay1pin = 21
relay2pin = 20
relay3pin = 16

def writerelay(relay,state):
	GPIO.setmode(GPIO.BCM)
#	GPIO.setup(relay2pin,GPIO.OUT,initial=GPIO.HIGH)
	#GPIO.setup(relay3pin,GPIO.OUT,initial=GPIO.HIGH)
	#GPIO.setup(relay3pin,GPIO.IN)
	GPIO.setup(relay,GPIO.OUT,initial=GPIO.HIGH)
	GPIO.output(relay,state)
#	GPIO.output(relay,GPIO.HIGH)
	#print GPIO.input(relay2pin)
	#print GPIO.input(relay3pin)
	#print GPIO.input(27)

#	sleep(2)
#	GPIO.output(relay1pin,GPIO.HIGH)
#	GPIO.output(relay2pin,GPIO.LOW)
#	sleep(2)
#	GPIO.output(relay2pin,GPIO.HIGH)
	GPIO.cleanup()

if __name__=="__main__":
  if len(argv) < 3:
     exit(1)
  else:
    writerelay(argv[1],argv[2]) 
  
