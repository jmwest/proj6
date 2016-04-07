# Navigate to pagerank folder
cd pagerank

# Make pagerank.net if it doesn't exist
echo "Looking for pagerank/pagerank_code/pagerank.net ..."
if [ -e "pagerank_code/pagerank.net" ]; then
	echo "  Found pagerank.net."
else
	echo "  Could not find pagerank.net."
	echo "  Executing edges.py."
	echo "  This might take a few minutes..."
	python edges.py ../data/mining.edges.xml > pagerank_code/pagerank.net
fi
echo ""

# Run pagerank if necessary
echo "Looking for pagerank/pagerank_code/output.txt ..."
if [ -e "pagerank_code/p6_output.txt" ]; then
	echo "  Found p6_output.txt."
else
	echo "  Could not find p6_output.txt."
	echo "  Running pagerank program."
	make run_pagerank
fi
echo ""

# Check to make sure p6_output.txt is the correct amount of lines
NUM_LINES=$(wc -l pagerank_code/p6_output.txt | awk '{print $1}')
CORRECT_NUM_LINES=$(echo "30109")
echo "Checking if p6_output.txt has correct amount of lines..."
if [ "$NUM_LINES" = "$CORRECT_NUM_LINES" ]; then
	echo "  Success! p6_output.txt has $NUM_LINES lines."
else
	echo "  Incorrect amount of lines: $NUM_LINES"
fi

# Navigate back to root
cd ..