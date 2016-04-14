import requests
import json
from flask import *
from extensions import mysql
from globals import *


wikipedia = Blueprint('wikipedia', __name__, template_folder='templates')

@wikipedia.route(route_prefix + '/wikipedia', methods=['GET'])
def wikipedia_route():

	numberOfHits = 0
	listOfHits = []

	options = {
		"searched": False,
		"deep_copy": False,
		"numHits": 0,
		"hits": listOfHits,
	}

	if request.args.get('q'):
		if request.args.get('w'):
			
			q = str(request.args.get('q'))
			w = str(request.args.get('w'))
			
			options['q'] = q
			options['w'] = w
			
			print "Received wikipedia search request:"
			print "  q: " + q
			print "  w: " + w
			print ""

			index_server_url = 'http://localhost:3002/search?q=' + q + '&w=' + w
			print "Making request to index_server..."
			print "  url: " + index_server_url
			result = requests.get(index_server_url)
			result_text = result.text 
			print "  " + result_text
			print ""

			result_json = json.loads(result_text)

			options["searched"] = True
			options["numHits"] = len(result_json["hits"])
			options["hits"] = result_json["hits"]

			for hit in options["hits"]:
				# hit["caption"] = captions[ int(hit["id"]) - 1 ].decode("utf8")
				cur = mysql.connection.cursor()

				select_stmt = "SELECT title, summary "
				select_stmt += "FROM Documents "
				select_stmt += "WHERE docid = %(hitId)s"
				cur.execute(select_stmt, { 'hitId': hit["id"] })

				cur_result = cur.fetchall()[0]
				
				summary_string = cur_result[1]

				hit["title"] = cur_result[0]
				hit["summary"] = summary_string[:200]

	return render_template("wikipedia.html", **options)

##############################
# I probably need to add in  #
# some checks to make sure   #
# the doc_id is a valid id   #
# before displaying the page #
##############################
@wikipedia.route(route_prefix + '/wikipedia/summary/<doc_id>', methods=['GET'])
def wikipedia_deep_summary_route(doc_id):
	
	listOfHits = []
	
	options = {
		"searched": False,
		"deep_copy": True,
		"numHits": 0,
		"hits": listOfHits,
	}
	
	cur = mysql.connection.cursor()
			
	select_stmt = "SELECT title, categories, image, summary "
	select_stmt += "FROM Documents "
	select_stmt += "WHERE docid = %(hitId)s"
	cur.execute(select_stmt, { 'hitId': doc_id })
	
	cur_result = cur.fetchall()[0]
	
	document = {
		"doc_id": doc_id,
		"title": cur_result[0],
		"categories": cur_result[1],
		"image": cur_result[2],
		"summary": cur_result[3]
	}
	
	options['document'] = document
	
	index_server_url = 'http://localhost:3002/search?q=' + document['title'] + '&w=0.15'
	print "Making request to index_server..."
	print "  url: " + index_server_url
	result = requests.get(index_server_url)
	result_text = result.text
	print "  " + result_text
	print ""
	
	result_json = json.loads(result_text)

	options["numHits"] = len(result_json["hits"])
	options["hits"] = result_json["hits"]

	# NEED TO MAKE SURE THAT THE CURRENT DOCUMENT DOESN'T
	# GET INCLUDED IN THE 10 DOCS
	for hit in options["hits"]:
		# hit["caption"] = captions[ int(hit["id"]) - 1 ].decode("utf8")
		cur = mysql.connection.cursor()
		
		select_stmt = "SELECT title "
		select_stmt += "FROM Documents "
		select_stmt += "WHERE docid = %(hitId)s "
		cur.execute(select_stmt, { 'hitId': hit["id"] })
		
		cur_result = cur.fetchall()[0]
		
		hit["title"] = cur_result[0]

	return render_template("wikipedia.html", **options)
