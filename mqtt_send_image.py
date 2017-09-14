#!/usr/bin/env python

import paho.mqtt.client as mqtt

mqttc = mqtt.Client()

mqttc.connect("anttgrid.com", 1883)



f=open("b.jpg", "rb")
fileContent = f.read()
byteArr = bytearray(fileContent)
#print byteArr
mqttc.loop_start()
mqttc.publish("eyegrid/rpi", byteArr)
mqttc.loop_stop()
mqttc.disconnect()

