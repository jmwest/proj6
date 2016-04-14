cd mapreduce

cat intermediate/part-* | sort > intermediate.txt
cat intermediate2/part-* | sort > intermediate2.txt
cat output/part-* | sort > output.txt

cat test_intermediate/part-* | sort > test_intermediate/intermediate.txt
cat test_output/part-* | sort > test_output/output.txt

cd ..
