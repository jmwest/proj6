#goes through the data and outputs the number of docs it found
import sys

docCount = 0

for line in sys.stdin:
	try:
		docID = int(line)
		ticker += 1	
	except:
		pass	

print docCount
print
