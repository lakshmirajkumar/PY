import paho.mqtt.client as mqtt
import json
import MySQLdb


db = MySQLdb.connect("localhost","root","1234","datagrid" )
cursor = db.cursor()

def on_connect(client, userdata, rc):
    print("Connect" + str(rc))
    client.subscribe("contacts") 

def on_message(client, userdata, msg):
    print "Topic : ", msg.topic
    resp = json.loads(msg.payload)
    for num in range(0,len(resp['Contacts'])):
   # 	print resp['Contacts'][num]["phone"]
	sql = "select json_resp from tc_master where num='%s' " % (resp['Contacts'][num]["phone"])
	print sql
        try:
           cursor.execute(sql)
	   contact_data=cursor.fetchall()
	   for row in contact_data:
		json_resp=row[0].encode("utf-8")
	   	print json_resp
        except:
           db.rollback()
	

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("anttgrid.com", 1883)

client.loop_forever()
db.close()
