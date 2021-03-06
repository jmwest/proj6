#!/usr/bin/python

#this script takes in xml files with documents, in this format:
#<eecs485_article>
	# <eecs485_article_id>123456789</eecs485_article_id>
	# <eecs485_article_title>Donald J Trump</eecs485_article_title>
	# <eecs485_article_body>When it comes to great steaks, I've just raised the stakes</eecs485_article_body>
#</eecs485_article>

#this script outputs the words with info, in this format:

#number of docs this mapper read
#5
#word 		doc appearance 			# of appearances in that doc
# -------------------------------------------------------------------
# baltimore			101					3
# baltimore			393					1
# alabama			101					1
# alabama			202					4
# alabama			290					2
# california		202					40	
# bolivia			101					33
# afghanistan		939					399	


import os 
import sys

def removeNonAlphaNumeric(line):
	for char in line:
		if not char.isalnum() and char != ' ':
			line = line.replace(char, '')
	return line


mapForAllWords = {}
ticker = 0
docID = -1

listOfStopWords = []
for line in open('mapreduce/stopwords.txt', 'r'):
	line = removeNonAlphaNumeric(line)
	listOfStopWords.append(line)

for line in sys.stdin:

	# DocId
	if ticker == 0:
		try:
			docID = int(line)
			ticker += 1	
		except:
			pass

	# Title
	elif ticker == 1:
		titleForThisDoc = line
		ticker += 1

	# Body
	elif ticker == 2:

		line = removeNonAlphaNumeric(line)
		
		#lowercase everything
		line = line.lower()

		fullBody = line.split()
		for word in fullBody:
			#if not stop word, add to mapForAllWords
		 	if word not in listOfStopWords:
				# if word == 'sciences':
					# print "Found sciences"
				if word in mapForAllWords:
					if docID in mapForAllWords[word]:
						mapForAllWords[word][docID] = mapForAllWords[word][docID] + 1
					else:
						mapForAllWords[word][docID] = 1
				else:
					mapForAllWords[word] = {}
					mapForAllWords[word][docID] = 1
		ticker = 0


#print everything to output
for word in mapForAllWords:
	# if word == 'sciences':
		# print mapForAllWords[word]
	for docID in mapForAllWords[word]:
		print word + "\t" + str(docID) + "\t" + str(mapForAllWords[word][docID])
