import xml.etree.ElementTree as ET
import os
import sys

treeArticles = ET.parse('../../data/mining.articles.xml')
articles = treeArticles.getroot()

ticker = 0
spotWithinFile = 0
articlesPerFile = int(sys.argv[1])
file = open('splitArticles/articleFile'+str(ticker), 'w')

for article in articles:
	for articleAttribute in article:
		if articleAttribute.tag == 'eecs485_article_id':
			if articleAttribute.text:
				file.write(articleAttribute.text + '\n')

		if articleAttribute.tag == 'eecs485_article_title':
			if articleAttribute.text:
				file.write(articleAttribute.text + '\n')
			else:
				file.write('\n')
			
		elif articleAttribute.tag == 'eecs485_article_body':
			bodyString = articleAttribute.text.replace('\n', ' ')
			file.write(bodyString)
			file.write('\n')
	spotWithinFile += 1
	if spotWithinFile == articlesPerFile:
		ticker += 1
		spotWithinFile = 0
		file = open('splitArticles/articleFile'+str(ticker), 'w')


	

# <eecs485_article_id>303</eecs485_article_id>
# <eecs485_article_title>Alabama</eecs485_article_title>
# <eecs485_article_body>