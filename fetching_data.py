import MySQLdb
import json
import paho.mqtt.client as mqtt
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect("localhost","root","1234","datagrid",charset='utf8',use_unicode=True)

  def query(self, sql):
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)
      rows=cursor.fetchall()
      for row in rows:
              num=row[0]
              gender=row[1]
              score=row[2]
              flags=row[3]
              dc=row[4]
              cc=row[5]
              zip=row[6]
              tag1=str(row[7])
              tag2=str(row[8])
              ptime=str(row[9])
              mtime=str(row[10])
              json_resp=row[11].encode("utf-8")
              json_data="{\"num\":"+num+','+"\"gender\":"+gender+','+"\"score\":"+str(score)+','+"\"flags\":"+str(flags)+','+"\"dc\":"+str(dc)+','+"\"cc\":"+cc+','+"\"tag1\":"+tag1+','+"\"tag2\":"+tag2+','+"\"ptime\":"+ptime+','+"\"mtime\":"+mtime+','+"\"json_resp\":"+json_resp
              client.publish("Antin/smsgrid/data",json_data)

    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
      rows=cursor.fetchall()
      for row in rows:
              num=row[0]
              gender=row[1]
              score=row[2]
              flags=row[3]
              dc=row[4]
              cc=row[5]
              zip=row[6]
              tag1=str(row[7])
              tag2=str(row[8])
              ptime=str(row[9])
              mtime=str(row[10])
              json_resp=row[11].encode("utf-8")
              json_data="{\"num\":"+num+','+"\"gender\":"+gender+','+"\"score\":"+str(score)+','+"\"flags\":"+str(flags)+','+"\"dc\":"+str(dc)+','+"\"cc\":"+cc+','+"\"tag1\":"+tag1+','+"\"tag2\":"+tag2+','+"\"ptime\":"+ptime+','+"\"mtime\":"+mtime+','+"\"json_resp\":"+json_resp
              client.publish("Antin/smsgrid/data",json_data)

    return cursor



db = DB()

def on_disconnect(client, userdata, rc):
        if rc != 0:
                print("Unexpected disconnection.")
        client.reconnect()

def on_connect(client, userdata,flags, rc):
        print("Connected with result code "+str(rc))
        client.subscribe("Antin/smsgrid/request")

def on_message(client, userdata, msg):

        print "Topic: ", msg.topic+'\nMessage: '+str(msg.payload)
        sql = "select * from tc_master where num='%s'" % (str(msg.payload))
	db.query(sql)


client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect=on_disconnect
client.on_message = on_message
client.connect("anttgrid.com", 1883, 60)
client.loop_forever()
db.close()
