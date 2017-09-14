import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print("Connect" + str(rc))
    client.subscribe("eyegrid/rpi") 

def on_message(client, userdata, msg):
    print "Topic : ", msg.topic
    f = open("output.jpg", "w")  #there is a output.jpg which is different
    f.write(msg.payload)
    f.close()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("anttgrid.com", 1883)

client.loop_forever()
