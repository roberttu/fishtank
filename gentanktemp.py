#!/usr/bin/python

from string import split

f=open("/sys/bus/w1/devices/w1_bus_master1/28-051686b8acff/w1_slave","r")
temp= float(split(f.read(),"t=")[1])/1000*9/5+32
f2=open("/home/pi/tanktemp.txt","w")
f2.write(str(temp))
f2.close()
