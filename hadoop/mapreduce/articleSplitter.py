import xml.etree.ElementTree as ET
import os
import sys

treeArticles = ET.parse('miningArticlesExample.xml')
articles = treeArticles.getroot()

ticker = 0
spotWithinFile = 0
articlesPerFile = int(sys.argv[1])
file = open('splitArticles/articleFile'+str(ticker), 'w')

for article in articles:
	file.write("<"+article.tag+">\n")
	for articleAttribute in article:
		file.write("\t<"+articleAttribute.tag+">"+articleAttribute.text+"</"+articleAttribute.tag+">\n")
	spotWithinFile += 1
	file.write("\n</"+article.tag+">\n")
	if spotWithinFile == articlesPerFile:
		ticker += 1
		print "lol"
		spotWithinFile = 0
		file = open('splitArticles/articleFile'+str(ticker), 'w')
	

