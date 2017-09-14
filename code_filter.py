import sys

f = open( sys.argv[1], 'rU' ) #open the file in read universal mode
for line in f:
	cells = line.split( "|" )
	sys.stdout.write(cells[0])
#	if sys.argv[2] in cells[1] :
#		print cells[0]+','+cells[1][0:6]

f.close()

