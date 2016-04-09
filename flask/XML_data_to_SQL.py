#
import os
import hashlib
import shutil
import xml.etree.ElementTree as ET
import sys

data_dir = './data/'

#articles_array = []
articles_dict = {}

# Parse the mining.articles.xml file
articles_tree = ET.parse(data_dir + 'mining.articles.xml')

articles_root = articles_tree.getroot()

for article in articles_root:
	
	docid_text = article.find('eecs485_article_id').text
	dict = {
		'docid': docid_text,
		'title': article.find('eecs485_article_title').text,
		'categories': '',
		'image': '',
		'summary': ''
	}
	
#	articles_array.append(dict)
	articles_dict[docid_text] = dict

print 'mining.articles.xml complete'

# Parse the mining.category.xml file
categories_tree = ET.parse(data_dir + 'mining.category.xml')

categories_root = categories_tree.getroot()

for category in categories_root:
	
	category_string = ''
	if category.find('eecs485_article_category') is not None:
		category_string = category.find('eecs485_article_category').text
	
#	if category_string != '':
#		category_string = category_string[:-2]

	docid_text = category.find('eecs485_article_id').text
	
	if articles_dict[docid_text]['categories'] != '':
		articles_dict[docid_text]['categories'] = articles_dict[docid_text]['categories'] + ', ' + category_string
	else:
		articles_dict[docid_text]['categories'] = category_string

#	for article in articles_array:
#
#		if article['docid'] == category.find('eecs485_article_id').text:
#			article['categories'] = category_string
#			break

print 'mining.category.xml complete'

# Parse the mining.imageUrls.xml file
images_tree = ET.parse(data_dir + 'mining.imageUrls.xml')

images_root = images_tree.getroot()

for image in images_root:
	
	url_string = ''
	image_url = image.find('eecs485_pngs')
	if image_url is not None:
		if image_url.find('eecs485_png_url') is not None:
			url_string = image_url.find('eecs485_png_url').text

	docid_text = image.find('eecs485_article_id').text
	articles_dict[docid_text]['image'] = url_string
#	for article in articles_array:
#		
#		if article['docid'] == image.find('eecs485_article_id').text:
#			article['image'] = url_string
#			break

print 'mining.imageUrls.xml complete'

# Parse the mining.infobox.xml file
infobox_tree = ET.parse(data_dir + 'mining.infobox.xml')

infobox_root = infobox_tree.getroot()

for box in infobox_root:
	
	summary_string = ''
	summary = box.find('eecs485_article_summary')
	if summary is not None:
		summary_string = summary.text

	docid_text = box.find('eecs485_article_id').text
	articles_dict[docid_text]['summary'] = summary_string
#	for article in articles_array:
#		
#		if article['docid'] == box.find('eecs485_article_id').text:
#			article['summary'] = summary_string
#			break

print 'mining.infobox.xml complete'

# Output SQL commands to wikipedia.sql
#output_string = 'CREATE TABLE Documents\n'
#output_string += '(\n\tdocid int,'
#output_string += '\n\ttitle varchar(100),'
#output_string += '\n\tcategories varchar(5000),'
#output_string += '\n\timage varchar(200),'
#output_string += '\n\tsummary varchar(5000),'
#output_string += '\n\tPRIMARY KEY (docid)\n);\n\n'

insert_string = ''
#for article in articles_array:
#	insert_string += 'INSERT INTO Documents\nVALUES ('
#	insert_string += ('\'' + article['docid'] + '\', ')
#	insert_string += ('\'' + article['title'] + '\', ')
#	insert_string += ('\'' + article['categories'] + '\', ')
#	insert_string += ('\'' + article['image'] + '\', ')
#	insert_string += ('\'' + article['summary'] + '\'')

for key, value in articles_dict.iteritems():
	insert_string += 'INSERT INTO Documents\nVALUES ('
	insert_string += ('\'' + value['docid'] + '\', ')
	
	if value['title'] is None:
		insert_string += ('\'\', ')
	else:
		insert_string += ('\'' + value['title'] + '\', ')

	if value['categories'] is None:
		insert_string += ('\'\', ')
	else:
		insert_string += ('\'' + value['categories'] + '\', ')

	if value['image'] is None:
		insert_string += ('\'\', ')
	else:
		insert_string += ('\'' + value['image'] + '\', ')
	
	if value['summary'] is None:
		insert_string += ('\'\');\n\n')
	else:
		insert_string += ('\'' + value['summary'] + '\');\n\n')


with open("./flask/sql/wikipedia.sql", 'w') as myfile:
	myfile.write(output_string)
	myfile.write(insert_string)

print 'write to flask/sql/wikipedia.sql complete'
