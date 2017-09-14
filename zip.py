import sys

f = open( sys.argv[1], 'rU' ) #open the file in read universal mode
for line in f:
#	sys.stdout.write(line)
	if  sys.argv[2] in line[11:18]:
		sys.stdout.write(line)

f.close()

