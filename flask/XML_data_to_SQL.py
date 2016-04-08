#
import os
import hashlib
import shutil
import xml.etree.ElementTree as ET
import sys

data_dir = './data/'

articles_array = []

# Parse the mining.articles.xml file
articles_tree = ET.parse(data_dir + 'mining.articles.xml')

articles_root = articles_tree.getroot()

for article in articles_root:
	
	dict = {
		'docid': article.find('eecs485_article_id').text,
		'title': article.find('eecs485_article_title').text,
		'categories': '',
		'image': '',
		'summary': ''
	}
	
	articles_array.append(dict)

print 'mining.articles.xml complete'

# Parse the mining.category.xml file
categories_tree = ET.parse(data_dir + 'mining.category.xml')

categories_root = categories_tree.getroot()

for category in categories_root:
	
	category_string = ''
	for article_category in category.findall('eecs485_article_category'):
		category_string += (article_category.text + ', ')
	
	if category_string != '':
		category_string = category_string[:-2]

	for article in articles_array:

		if article['docid'] == category.find('eecs485_article_id').text:
			article['categories'] = category_string

print 'mining.category.xml complete'

# Parse the mining.imageUrls.xml file
images_tree = ET.parse(data_dir + 'mining.imageUrls.xml')

images_root = images_tree.getroot()

for image in images_root:
	
	url_string = ''
	image_url = image.find('eecs485_pngs')
	if image_url is not None:
		url_string = image_url.find('eecs485_png_url').text

	for article in articles_array:
		
		if article['docid'] == image.find('eecs485_article_id').text:
			article['image'] = url_string

print 'mining.imageUrls.xml complete'

# Parse the mining.infobox.xml file
infobox_tree = ET.parse(data_dir + 'mining.infobox.xml')

infobox_root = infobox_tree.getroot()

for box in infobox_root:
	
	summary_string = ''
	summary = box.find('eecs485_article_summary')
	if summary is not None:
		summary_string = summary.text
	
	for article in articles_array:
		
		if article['docid'] == summary.find('eecs485_article_id').text:
			article['summary'] = summary_string

print 'mining.infobox.xml complete'

# Output SQL commands to wikipedia.sql
output_string = 'CREATE TABLE Documents\n'
output_string += '(\n\tdocid int,\n'
output_string += '\n\ttitle varchar(100),\n'
output_string += '\n\tcategories varchar(5000),\n'
output_string += '\n\timage varchar(200),\n'
output_string += '\n\tsummary varchar(5000),\n'
output_string += '\n\tPRIMARY KEY (docid)\n);\n\n'

insert_string = ''
for article in articles_array:
	insert_string += 'INSERT INTO Documents\nVALUES ('
	insert_string += ('\'' + article['docid'] + '\', ')
	insert_string += ('\'' + article['title'] + '\', ')
	insert_string += ('\'' + article['categories'] + '\', ')
	insert_string += ('\'' + article['image'] + '\', ')
	insert_string += ('\'' + article['summary'] + '\'')

with open("sql/wikipedia.sql", "r") as myfile:
	myfile.write(output_string)
	myfile.write(insert_string)

print 'write to sql/wikipedia.sql complete'
