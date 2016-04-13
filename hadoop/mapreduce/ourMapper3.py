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

for line in sys.stdin:
	words = line.split()
	# If it's a newline, skip it
	if (len(words) < 6):
		continue

	output = words[1] + '\t'
	output += words[3] + '\t'
	output += words[2] + '\t'
	output += words[0] + '\t'
	output += words[4] + '\t'
	output += words[5] + '\t'

	print output