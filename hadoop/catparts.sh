cd mapreduce

cat intermediate/part-* | sort > intermediate.txt
cat output/part-* | sort > output.txt

cd ..