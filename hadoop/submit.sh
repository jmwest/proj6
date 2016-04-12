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