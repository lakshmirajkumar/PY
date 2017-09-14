import sys
import numpy as np


f = open( sys.argv[1], 'rU' ) #open the file in read universal mode
for line in f:
	cells = line.split( "|" )
	addr=cells[5]
	code=addr[-6:]
	print cells[2]
f.close()

