import csv
import requests 
import re
import os
import sys
import json
from urllib import urlopen

def writetocsv():
	f = open('data.json')
	data = json.load(f)
	f.close()
	f = csv.writer(open('data.csv', 'wb+'))
	for item in data:
    		values = [ x.encode('utf8') for x in item['fields'].values() ]
    		f.writerow([item['pk'], item['model']] + values)

def writetofile():
	with open(sys.argv[1]) as csvDataFile:
    		csvReader = csv.reader(csvDataFile)
    		for row in csvReader:
			url="http://139.59.24.213:3000/TCX/%s" % (row[0])
			r = requests.get(url)
	#		with open("data.json","a") as json:
	#			json.write(http_document)		
	#			json.write("\n")
			print row[0]	


if __name__ == "__main__":
	print "writing into file"
	writetofile()
	print "Done"
	#writetocsv()
