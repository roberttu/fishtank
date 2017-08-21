#!/usr/bin/python

import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import json, time
import pdb

# device credentials
device_id        = 'skimmer'      # * set your device id (will be the MQTT client username)
device_secret    = '<DEVICE_SECRET>'  # * set your device secret (will be the MQTT client password)
random_client_id = '<CLIENT_ID>'      # * set a random client_id (max 23 char)

# -------------- #
# Board settings #
# -------------- #
#buttonPin = 7
relayPin = 14

GPIO.setmode(GPIO.BCM)  # use P1 header pin numbering convention
GPIO.cleanup()            # clean up resources
GPIO.setup(relayPin, GPIO.OUT)   # relay pin setup
#GPIO.setup(buttonPin, GPIO.IN)   # button pin setup


# --------------- #
# Callback events #
# --------------- #

# connection event
def on_connect(client, data, flags, rc):
    print('Connected, rc: ' + str(rc))

# subscription event
def on_subscribe(client, userdata, mid, gqos):
    print('Subscribed: ' + str(mid))
    # confirm changes to Leylan
#    message={'payload':73}
#    client.publish("fishtank/skimmer/get", payload=json.dumps(message))

# received message event
def on_message(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
#    pdb.set_trace()
#    value = json.loads(json_data)['payload']
#    value = json.loads(json_data)['payload']
    value = json_data
    if value == 'ON':
        relay_status = GPIO.LOW
        GPIO.output(relayPin, GPIO.LOW)
        print "switch turned on\n"
    else:
        relay_status = GPIO.HIGH
        GPIO.output(relayPin, GPIO.HIGH)
        print "switch turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic, json_data)


# ------------- #
# MQTT settings #
# ------------- #

# create the MQTT client
client = paho.Client(client_id=random_client_id, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe


# device topics
in_topic  = 'fishtank/' + device_id + '/command'  # receiving messages
out_topic = 'fishtank/' + device_id + '/state'  # publishing messages

# client connection
#client.username_pw_set(device_id, device_secret)  # MQTT server credentials
client.connect("192.168.1.188")                   # MQTT server address
client.subscribe(in_topic, 0)                     # MQTT subscribtion (with QoS level 0)

# ------------ #
# Button logic #
# ------------ #

prev_status = GPIO.LOW
relay_status  = GPIO.LOW
updated_at  = 0  # the last time the output pin was toggled
debounce    = 0.2  # the debounce time, increase if the output flickers

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
#    button = GPIO.input(buttonPin)

#    if button != prev_status and time.time() - updated_at > debounce:
#        prev_status = button
#        updated_at  = time.time()
#
#        if button:
#            relay_status = not relay_status
#            button_payload = 'off'
#            if relay_status == GPIO.HIGH:
#                button_payload = 'on'
#            # effectively update the light status
#            GPIO.output(relayPin, relay_status)
#            payload = { 'properties': [{ 'id': '518be5a700045e1521000001', 'value': button_payload }] }
#            client.publish(out_topic, json.dumps(payload))

print('rc: ' + str(rc))


