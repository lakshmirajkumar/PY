#!/usr/bin/python
import sys
import numpy as np
import MySQLdb

#db = MySQLdb.connect("localhost","datagrid","datagrid@4321","datagrid" )
db = MySQLdb.connect("localhost","root","1234","datagrid" )

cursor = db.cursor()

f = open( sys.argv[1], 'rU' ) 
for line in f:
	cells = line.split( "|" )
	number='91'+cells[0]
	njson= '{'+"\n\"Name\":\""+cells[2]+"\","+"\"Father/Husbends_Name\" :\""+cells[4]+"\","+"\"Tele\" :"+'{'+"\"Home\" :\""+cells[0]+"\","+"\"Alt\" :\""+cells[7]+"\"},"+"\"Dob\" :\""+cells[3]+"\","+"\"E-mail\" :\""+cells[8]+"\","+"\"Gender\" :\""+cells[9]+"\","+"\"Address\" : {\"Local\" :\"" +cells[5]+"\","+"\"Permanent\" :\"" +cells[6]+"\"},"+"\"Nationality\" :\""+cells[10]+"\",\"Linkdin\": {\"Link\" :\" \",\"hcard\":{\"fn\":\" \",\"photo\":\" \",\"person\":{\"location\":\" \",\"org\":\" \",\"role\":\" \"}}}\n}"
#	njson="{\"Name\":\"\",\"Father/Husbends_Name\" :\"\",\"Tele\" :{\"Home\" :\"\",\"Alt\" :\"\"},\"Dob\" :\"\",\"E-mail\" :\"\",\"Gender\" :\"\",\"Address\" : {\"Local\" :\"\",\"Permanent\" :\"\"},\"Nationality\" :\"\",\"Linkdin\": {\"Link\" :\" \",\"hcard\":{\"fn\":\" \",\"photo\":\" \",\"person\":{\"location\":\" \",\"org\":\" \",\"role\":\" \"}}}}"
	#print njson	
	sql = "update tc_master set njson_data='%s' " % (njson)
	print sql
	try:
	   cursor.execute(sql)
	   db.commit()
	except:
	   db.rollback()
f.close()
db.close()

