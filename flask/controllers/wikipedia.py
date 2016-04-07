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
		"numHits": 0,
		"hits": listOfHits
	}

	if request.args.get('q'):
		q = str(request.args.get('q'))
		print "Found q request. q: " + q

		print ""
		result = requests.get('http://localhost:3002/search?q=' + q)
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

			select_stmt = "SELECT url, caption, filename "
			select_stmt += "FROM PhotoSearch "
			select_stmt += "WHERE sequencenum = %(hitId)s"
			cur.execute(select_stmt, { 'hitId': hit["id"]  })

			cur_result = cur.fetchall()[0]

			hit["url"] = cur_result[0]
			hit["caption"] = cur_result[1]
			hit["filename"] = cur_result[2]


	return render_template("wikipedia.html", **options)