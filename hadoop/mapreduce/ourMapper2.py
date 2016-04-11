#reads in from a text file with this format:
# word | idf | total occurences in our entire database | docID | occurences in doc | docID | occrences in doc| doc ID....

#outputs to standard output lines in the following format:
# word | idf | total occurences in our entrie databse | docID | occurences in doc | preSquareRootNormalization | docID | occurences in doc | preSquareRootNormalization |docID | occurences in doc | preSquareRootNormalization |.....

import os
import sys

#key: docID     value: [[word, tf2id2],[word, tf2id2],[word, tf2id2]...] 
dictionaryOfDocIDs = {}

#key: word 		value: idf, total occurences, [[docID, occurences in doc, preSquareRootNormalization]...]
finalOutput = {}

#key: docID  	value: SUM(tf2idf2)
dictionaryOfDoc_tf2idf2_Sums = {}

#go through every line in the file
for line in sys.stdin:
	lineAsListOfWords = line.split()

	#save each word into a separate data structure
	finalOutput[lineAsListOfWords[0]] = [lineAsListOfWords[1], lineAsListOfWords[2], []]


	#skip the first 3 words in list, then go through the list by 2s
	i = 3
	for doc in lineAsListOfWords[3::2]:
		#add that doc to the word's line for final output
		finalOutput[lineAsListOfWords[0]][2].append([doc, lineAsListOfWords[i+1], ])
		#find tf2idf2
		tf2 = int(lineAsListOfWords[i+1]) * int(lineAsListOfWords[i+1])
		idf2 = float(lineAsListOfWords[1]) * float(lineAsListOfWords[1])
		tf2idf2 = tf2 * idf2
		#if docID not in our dict already, add it
		if doc not in dictionaryOfDocIDs:
			dictionaryOfDocIDs[doc] = [[lineAsListOfWords[0], tf2idf2]]
		#if it's already in there, append this word
		else:
			dictionaryOfDocIDs[doc].append([lineAsListOfWords[0], tf2idf2])
		i += 2

	#we now have dictionaryOfDocIDS completed
	#now go through each doc, and find the sum of all the tf2idf2's 
	for docID in dictionaryOfDocIDs:
		SUMtf2idf2 = 0
		for tuple in dictionaryOfDocIDs[docID]:
			SUMtf2idf2 += tuple[1]
		dictionaryOfDoc_tf2idf2_Sums[docID] = SUMtf2idf2


#print each line of the inverted index file
for word in finalOutput:
	sys.stdout.write(word + ' ' + str(finalOutput[word][0]) + ' ' + str(finalOutput[word][1])) 
	for doc in finalOutput[word][2]:
		sys.stdout.write(' ' + str(doc[0]) + ' ' + str(doc[1]) + ' ' + str(dictionaryOfDoc_tf2idf2_Sums[doc[0]])) 
	print

# for doc in dictionaryOfDoc_tf2idf2_Sums:
# 	print doc
# 	print dictionaryOfDoc_tf2idf2_Sums[doc]
# 	print 


