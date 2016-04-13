#!/usr/bin/python

#Input: sys.read in the following format:
# docIDA | wordA | total occurences in our entrie database | idf  | occurences in doc |
# docIDA | wordB | total occurences in our entrie database | idf  | occurences in doc |
# docIDA | wordC | total occurences in our entrie database | idf  | occurences in doc |
# docIDB | wordA | total occurences in our entrie database | idf  | occurences in doc |
# docIDB | wordB | total occurences in our entrie database | idf  | occurences in doc |
# docIDC | wordD | total occurences in our entrie database | idf  | occurences in doc |
# docIDD | wordB | total occurences in our entrie database | idf  | occurences in doc |
# docIDD | wordD | total occurences in our entrie database | idf  | occurences in doc |

#Output: same thing, only with preSquareRootNormalization col at the end

import sys

#key: docID 		#value: preSquareRootNormalization score
dictionaryOfDocIDsToPreSquareScores = {}

#key: docID 		#value: dictionary { key: word   value: [total occurences in our entrie database | idf  | occurences in doc]}
finalOutput = {}

for line in sys.stdin:
	lineAsListOfCols = line.split()

	#make sure this doc is in our tf2idf2 dict
	if lineAsListOfCols[0] not in dictionaryOfDocIDsToPreSquareScores:
		dictionaryOfDocIDsToPreSquareScores[lineAsListOfCols[0]] = 0

	#get tf2idf2 of this word, for this doc
	tf = int(lineAsListOfCols[4])
	idf = float(lineAsListOfCols[3])
	tf2idf2 = tf * tf * idf * idf

	#add it to sum of all tf2idf2's for this doc
	dictionaryOfDocIDsToPreSquareScores[lineAsListOfCols[0]] += tf2idf2

	#make sure this doc is in our final output dict
	if lineAsListOfCols[0] not in finalOutput:
		finalOutput[lineAsListOfCols[0]] = {}

	#add this word and it's info to our finalOutput dict
	finalOutput[lineAsListOfCols[0]][lineAsListOfCols[1]] = [lineAsListOfCols[2], lineAsListOfCols[3], lineAsListOfCols[4]]


#print out what we got
for doc in finalOutput:
	for word in finalOutput[doc]:
		sys.stdout.write(doc + '\t' + word + '\t' + finalOutput[doc][word][0] + '\t' + finalOutput[doc][word][1] + '\t' + finalOutput[doc][word][2] + '\t' + dictionaryOfDocIDsToPreSquareScores[doc] + '\n')

































motto = '''
When it comes to great steaks, I've just raised the stakes.
The Sharper Image is one of my favorite stores, with fantastic products of all kinds.
That's why I'm thrilled they agree with me.
Trump Steaks are the world's greatest steaks and I mean that in every sense of the word.
And The Sharper Image is the only store where you can buy them.
Trump Steaks are by far the best tasting most flavorful beef you've ever had, truly in a league of their own.
Trump Steaks are five star gourmet, quality that belong in a very very select category of restaurant, and are Certified Angus Beef Prime.
There's nothing better than that.
Of all of the beef produced in America, less than one percent qualifies for that category.
It's the best of the best.
Until now you could only enjoy steaks of this quality in one of my resort restaurants or America's finest steakhouses, but now, that's changed.
Today through The Sharper Image, you can enjoy the world's greatest steaks, in your own home, with family, friends, anytime.
Trump Steaks are aged to perfection to provide the ultimate in tenderness and flavor.
If you like your steak, you'll absolutely love Trump Steaks.
Treat yourself to the very very best life has to offer.
And as a gift, Trump Steaks are the best you can give.
One bite and you'll know exactly what I'm talking about.
And believe me, I understand steaks, it's my favorite food, and these are the best.
'''


