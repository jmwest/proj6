#!/usr/bin/python

# Input format
# wordA | idf | #totalOccur | docIdA | #occurInDoc | presqrt
# wordA | idf | #totalOccur | docIdB | #occurInDoc | presqrt
# wordB | idf | #totalOccur | docIdA | #occurInDoc | presqrt
# 0     | 1   | 2           | 3      | 4           | 5

# Output format
# wordA | idf | #totalOccur | [ docIdA | #occurInDoc | presqrt ] | [ docIdB | #occurInDoc | presqrt ] ... 
# wordB | idf | #totalOccur | [ docIdA | #occurInDoc | presqrt ] | [ docIdB | #occurInDoc | presqrt ] ... 

import sys

def appendList(str_in, list_in):	
	for item in list_in:
		str_in += ' ' + item
	return str_in

# key: word
# val: str( idf | #totalOccur | [ docIdA | #occurInDoc | presqrt ] | [ docIdB | #occurInDoc | presqrt ] ... )
# This is a word, with the rest of the output
wordDict = {}

for line in sys.stdin:
	words = line.split()

	# If it's a newline, skip it
	if (len(words) < 6):
		continue

	word = words[0]

	# If word is in wordDict, append the last 3 indices to the end of val
	if word in wordDict:
		lastIndices = []
		lastIndices.append(words[3])
		lastIndices.append(words[4])
		lastIndices.append(words[5])
		wordDict[word] = appendList(wordDict[word], lastIndices)
		
	# If word is not in wordDict, add it, and append the last 5 indices to the end of val
	else:
		lastIndices = []
		lastIndices.append(words[1])
		lastIndices.append(words[2])
		lastIndices.append(words[3])
		lastIndices.append(words[4])
		lastIndices.append(words[5])
		wordDict[word] = appendList('', lastIndices)

for word in wordDict:
	print word, wordDict[word]