# Clean it out
rm -rf submit/
rm mapreduce.tar.gz

# Make the folders
mkdir submit
mkdir submit/mapreduce

# Copy files to a submit directory
cp mapreduce/ourMapper* submit/mapreduce
cp mapreduce/ourReducer* submit/mapreduce
cp mapreduce/stopwords.txt submit/mapreduce
cp run.sh submit/

# Compress it
tar -zcvf mapreduce.tar.gz submit

# pagerank.out
cp ../pagerank/pagerank_code/p6_output.txt pagerank.out

rm -rf submit/*
mv mapreduce.tar.gz submit/mapreduce.tar.gz
mv pagerank.out submit/pagerank.out