#!/usr/bin/python

import paho.mqtt.client as paho
import RPi.GPIO as GPIO
import json, time
import pdb

# device credentials
device_id        = 'skimmer'      # * set your device id (will be the MQTT client username)
device_id2        = 'fan'      # * set your device id (will be the MQTT client username)
device_id3        = 'pumps'      # * set your device id (will be the MQTT client username)
device_id4        = 'refillpump'      # * set your device id (will be the MQTT client username)
device_id5        = 'relay5'      # * set your device id (will be the MQTT client username)
device_id6        = 'relay6'      # * set your device id (will be the MQTT client username)
device_id7        = 'relay7'      # * set your device id (will be the MQTT client username)
device_id8        = 'relay8'      # * set your device id (will be the MQTT client username)
device_secret    = '<DEVICE_SECRET>'  # * set your device secret (will be the MQTT client password)
random_client_id = '<CLIENT_ID>'      # * set a random client_id (max 23 char)
random_client_id2 = '<CLIENT_ID2>'      # * set a random client_id (max 23 char)
random_client_id3 = '<CLIENT_ID3>'      # * set a random client_id (max 23 char)
random_client_id4 = '<CLIENT_ID4>'      # * set a random client_id (max 23 char)
random_client_id5 = '<CLIENT_ID5>'      # * set a random client_id (max 23 char)
random_client_id6 = '<CLIENT_ID6>'      # * set a random client_id (max 23 char)
random_client_id7 = '<CLIENT_ID7>'      # * set a random client_id (max 23 char)
random_client_id8 = '<CLIENT_ID8>'      # * set a random client_id (max 23 char)

# -------------- #
# Board settings #
# -------------- #
#buttonPin = 7
relayPin = 14
relayPin2 = 15
relayPin3 = 18
relayPin4 = 23
relayPin5 = 24
relayPin6 = 25
relayPin7 = 8
relayPin8 = 7

GPIO.setmode(GPIO.BCM)  # use P1 header pin numbering convention
GPIO.cleanup()            # clean up resources
GPIO.setup(relayPin, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin2, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin3, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin4, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin5, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin6, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin7, GPIO.OUT)   # relay pin setup
GPIO.setup(relayPin8, GPIO.OUT)   # relay pin setup
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
def on_message2(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin2, GPIO.LOW)
        print "switch2 turned on\n"
    else:
        GPIO.output(relayPin2, GPIO.HIGH)
        print "switch2 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic2, json_data)
def on_message3(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin3, GPIO.LOW)
        print "switch3 turned on\n"
    else:
        GPIO.output(relayPin3, GPIO.HIGH)
        print "switch3 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic3, json_data)
def on_message4(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin4, GPIO.LOW)
        print "switch4 turned on\n"
    else:
        GPIO.output(relayPin4, GPIO.HIGH)
        print "switch4 turned off\n"
    client.publish(out_topic4, json_data)
def on_message5(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin5, GPIO.LOW)
        print "switch5 turned on\n"
    else:
        GPIO.output(relayPin5, GPIO.HIGH)
        print "switch5 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic5, json_data)
def on_message6(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin6, GPIO.LOW)
        print "switch6 turned on\n"
    else:
        GPIO.output(relayPin6, GPIO.HIGH)
        print "switch6 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic6, json_data)
def on_message7(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin7, GPIO.HIGH)
        print "switch7 turned on\n"
    else:
        GPIO.output(relayPin7, GPIO.LOW)
        print "switch7 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic7, json_data)
def on_message8(client, obj, msg):
    # get the JSON message
    json_data = msg.payload
    # check the status property value
    print(json_data)
    value = json_data
    if value == 'ON':
        GPIO.output(relayPin8, GPIO.HIGH)
        print "switch8 turned on\n"
    else:
        GPIO.output(relayPin8, GPIO.LOW)
        print "switch8 turned off\n"

    # confirm changes to Leylan
    client.publish(out_topic8, json_data)


# ------------- #
# MQTT settings #
# ------------- #

# create the MQTT client
client = paho.Client(client_id=random_client_id, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_subscribe = on_subscribe

client2 = paho.Client(client_id=random_client_id2, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client2.on_message = on_message2
client2.on_connect = on_connect
client2.on_subscribe = on_subscribe
client3 = paho.Client(client_id=random_client_id3, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client3.on_message = on_message3
client3.on_connect = on_connect
client3.on_subscribe = on_subscribe
client4 = paho.Client(client_id=random_client_id4, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client4.on_message = on_message4
client4.on_connect = on_connect
client4.on_subscribe = on_subscribe
client5 = paho.Client(client_id=random_client_id5, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client5.on_message = on_message5
client5.on_connect = on_connect
client5.on_subscribe = on_subscribe
client6 = paho.Client(client_id=random_client_id6, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client6.on_message = on_message6
client6.on_connect = on_connect
client6.on_subscribe = on_subscribe
client7 = paho.Client(client_id=random_client_id7, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client7.on_message = on_message7
client7.on_connect = on_connect
client7.on_subscribe = on_subscribe
client8 = paho.Client(client_id=random_client_id8, protocol=paho.MQTTv31)  # * set a random string (max 23 chars)

# assign event callbacks
client8.on_message = on_message8
client8.on_connect = on_connect
client8.on_subscribe = on_subscribe

# device topics
in_topic  = 'fishtank/' + device_id + '/command'  # receiving messages
out_topic = 'fishtank/' + device_id + '/state'  # publishing messages
in_topic2  = 'fishtank/' + device_id2 + '/command'  # receiving messages
out_topic2 = 'fishtank/' + device_id2 + '/state'  # publishing messages
in_topic3  = 'fishtank/' + device_id3 + '/command'  # receiving messages
out_topic3 = 'fishtank/' + device_id3 + '/state'  # publishing messages
in_topic4  = 'fishtank/' + device_id4 + '/command'  # receiving messages
out_topic4 = 'fishtank/' + device_id4 + '/state'  # publishing messages
in_topic5  = 'fishtank/' + device_id5 + '/command'  # receiving messages
out_topic5 = 'fishtank/' + device_id5 + '/state'  # publishing messages
in_topic6  = 'fishtank/' + device_id6 + '/command'  # receiving messages
out_topic6 = 'fishtank/' + device_id6 + '/state'  # publishing messages
in_topic7  = 'fishtank/' + device_id7 + '/command'  # receiving messages
out_topic7 = 'fishtank/' + device_id7 + '/state'  # publishing messages
in_topic8  = 'fishtank/' + device_id8 + '/command'  # receiving messages
out_topic8 = 'fishtank/' + device_id8 + '/state'  # publishing messages

# client connection
#client.username_pw_set(device_id, device_secret)  # MQTT server credentials
client.connect("192.168.1.188")                   # MQTT server address
client.subscribe(in_topic, 0)                     # MQTT subscribtion (with QoS level 0)
client2.connect("192.168.1.188")                   # MQTT server address
client2.subscribe(in_topic2, 0)                     # MQTT subscribtion (with QoS level 0)
client3.connect("192.168.1.188")                   # MQTT server address
client3.subscribe(in_topic3, 0)                     # MQTT subscribtion (with QoS level 0)
client4.connect("192.168.1.188")                   # MQTT server address
client4.subscribe(in_topic4, 0)                     # MQTT subscribtion (with QoS level 0)
client5.connect("192.168.1.188")                   # MQTT server address
client5.subscribe(in_topic5, 0)                     # MQTT subscribtion (with QoS level 0)
client6.connect("192.168.1.188")                   # MQTT server address
client6.subscribe(in_topic6, 0)                     # MQTT subscribtion (with QoS level 0)
client7.connect("192.168.1.188")                   # MQTT server address
client7.subscribe(in_topic7, 0)                     # MQTT subscribtion (with QoS level 0)
client8.connect("192.168.1.188")                   # MQTT server address
client8.subscribe(in_topic8, 0)                     # MQTT subscribtion (with QoS level 0)
client.publish(out_topic, "OFF")
client2.publish(out_topic2, "OFF")
client3.publish(out_topic3, "OFF")
client4.publish(out_topic4, "OFF")
client5.publish(out_topic5, "OFF")
client6.publish(out_topic6, "OFF")
client7.publish(out_topic7, "ON")
client8.publish(out_topic8, "ON")
GPIO.output(relayPin, GPIO.LOW)
GPIO.output(relayPin2, GPIO.LOW)
GPIO.output(relayPin3, GPIO.LOW)
GPIO.output(relayPin4, GPIO.LOW)
GPIO.output(relayPin5, GPIO.LOW)
GPIO.output(relayPin6, GPIO.LOW)
GPIO.output(relayPin7, GPIO.LOW)
GPIO.output(relayPin8, GPIO.LOW)

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
    rc = rc+ client2.loop()
    rc =  rc+client3.loop()
    rc =  rc+client4.loop()
    rc =  rc+client5.loop()
    rc =  rc+client6.loop()
    rc =  rc+client7.loop()
    rc =  rc+client8.loop()
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
