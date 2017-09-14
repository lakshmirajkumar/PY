#!/usr/bin/env python

import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect("anttgrid.com", 1883)

f=open("b.webp", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)
#print byteArr
mqttc.loop_start()
mqttc.publish("image", byteArr)
mqttc.loop_stop()
mqttc.disconnect()

