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


import xml.etree.ElementTree as ET
import os 

mapForAllWords = {}
totalDocCount = 0

for fileName in os.listdir('input'):
	file = open('input/'+fileName, 'r')
	ticker = 0
	docID = -1
	for line in file:
		if ticker == 0:
			try:
				docID = int(line)
				ticker += 1	
			except:
				pass			
		elif ticker == 1:
			titleForThisDoc = line
			ticker += 1
		elif ticker == 2:
			#we're in body
			#remove non-alphanumeric chars
			for char in line:
				if not char.isalnum() and char != ' ':
					line = line.replace(char, '')
			
			#lowercase everything
			line = line.lower()
			fullBody = line.split()
			for word in fullBody:
				if word in mapForAllWords:
					if docID in mapForAllWords[word]:
						mapForAllWords[word][docID] = mapForAllWords[word][docID] + 1
				else:
					mapForAllWords[word] = {}
					mapForAllWords[word][docID] = 1
			ticker = 0
			totalDocCount += 1


#print everything to output
print totalDocCount
for word in mapForAllWords:
	for docID in mapForAllWords[word]:
		print word + "    " + str(docID) + "    " + str(mapForAllWords[word][docID])






#print final new line
print


#