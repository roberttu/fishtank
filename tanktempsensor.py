#!/usr/bin/python

from string import split
import paho.mqtt.client as mqtt
import json

f=open("/sys/bus/w1/devices/w1_bus_master1/28-051686b8acff/w1_slave","r")
temp= round(float(split(f.read(),"t=")[1])/1000*9/5+32,2)
client=mqtt.Client(client_id="fishtankpi")
client.connect("192.168.1.188", port=1883, keepalive=60)
message={'temperature':temp}
client.publish("fishtank/temperature", payload=json.dumps(message),retain=False)

#f2=open("/home/pi/tanktemp.txt","w")
#f2.write(str(temp))
#f2.close()
