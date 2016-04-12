#!/usr/bin/python

#goes through the data and outputs the number of docs it found
import sys

docCount = 0
ticker = 0

wordDict = {}

for line in sys.stdin:
	if (ticker % 3 == 0):
		docId = int(line)
		docCount += 1

	# elif (ticker % 3 == 2):
	# 	line_array = line.split()

	# 	for word in line_array:
	# 		if word in wordDict:
	# 			wordDict[word] += 1
	# 		else:
	# 			wordDict[word] = 1

	ticker += 1

# for word in wordDict:
# 	with open('mapreduce/n_k/' + word, 'w') as myfile:
# 		myfile.write(str(wordDict[word]) + '\n')

print docCount