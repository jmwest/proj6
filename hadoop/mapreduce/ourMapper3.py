#!/usr/bin/python

# Input format
# docIdA | wordA | #totalOccur | idf | #occurInDoc | presqrt
# docIdA | wordB | #totalOccur | idf | #occurInDoc | presqrt
# docIdB | wordA | #totalOccur | idf | #occurInDoc | presqrt
# 0      | 1     | 2           | 3   | 4           | 5

# Output format
# wordA | idf | #totalOccur | docIdA | #occurInDoc | presqrt
# wordA | idf | #totalOccur | docIdB | #occurInDoc | presqrt
# wordB | idf | #totalOccur | docIdA | #occurInDoc | presqrt
# 1     | 3   | 2           | 0      | 4           | 5

import sys

ticker = 0

for line in sys.stdin:
	words = line.split()

	ticker += 1
	# If it's a newline, skip it
	if (len(words) < 6):
		continue

	output = str(words[1]) + '\t'
	output += str(words[3]) + '\t'
	output += str(words[2]) + '\t'
	output += str(words[0]) + '\t'
	output += str(words[4]) + '\t'
	output += str(words[5]) + '\t'

	print output