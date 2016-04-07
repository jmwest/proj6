# Make sure you are in the root directory.
# NOTE: Everything is in index_server/p6test so it's completely self-contained.

# Pagerank
PAGERANK_PATH=../pagerank/
XML_FILE=p6test/1_test.xml
PAJEK_SCRIPT=../pagerank/edges.py
PAGERANK_NET=p6test/2_pagerank.net
PAGERANK_CONFIG=p6test/3_config.pagerank
PAGERANK_SCORES=p6test/4_scores.txt

# Index Server (TFIDF)
CAPTIONS_TXT=p6test/5_captions.txt
INVERTED_INDEX=p6test/6_inverted_index.txt

# Actual hits
SEARCH_RESULTS=p6test/7_results.json

# Query to search
query="pizza"

# 0 <= w <= 1. score = w*PR(d) + (1-w)*SIM(query, d)
weight="0.4"

# URL to request for query
URL="http://localhost:3002/search?q=$query&w=$weight"

# Navigate to index_server.
cd index_server

echo "Making pagerank.net ..."
python $PAJEK_SCRIPT $XML_FILE > $PAGERANK_NET
echo "Done."
echo ""

echo "Running pagerank ..."
make -C $PAGERANK_PATH p6
echo "Done."

echo "Searching for CPP process on $(whoami)..."
CPP_PID=$(ps aux | grep $(whoami) | grep 'indexServer' | awk '{print $2}')
if [ -z "$CPP_PID" ]; then
	echo "No C++ process found."
else
	kill $CPP_PID
	echo "C++ process terminated."
fi

echo "Making inverted index file and starting server ..."
make p6
echo "Done."
echo ""

# Make a query request and store the output.
curl -H "Accept: application/json" $URL > $SEARCH_RESULTS

# Go back to root.
cd ..