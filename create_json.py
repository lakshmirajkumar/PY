import sys
import numpy as np


f1 = open( sys.argv[1], 'rU' ) 
for line in f1:
	cells = line.split( "|" )
	data= '{'+"\n\"Name\":"+cells[2]+','+"\"Father/Husbend's_Name\" :"+cells[4]+','+"\"Tele\" :"+'{'+"\"Home\" :"+cells[0]+','+"\"Alt\" :"+cells[7]+"},"+"\"Dob\" :"+cells[3]+','+"\"E-mail\" :"+cells[8]+','+"\"Gender\" :"+cells[9]+','+"\"Address\" : {\"Local\" :" +cells[5]+','+"\"Permanent\" :" +cells[6]+"},"+"\"Nationality\" :"+cells[10]+",\"Linkdin\": {\"Link\" :\" \",\"hcard\":{\"fn\":\" \",\"photo\":\" \",\"person\":{\"location\":\" \",\"org\":\" \",\"role\":\" \"}}}\n}"


	print data
f1.close()

	

