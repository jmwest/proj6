# Has to be set so that we can run hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-oracle

#################################### 10 DOCS ####################################

# Hadoop doesn't like to clobber
rm -rf mapreduce/graded/empty
rm -rf mapreduce/graded/10docs_*

# Job 0
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/graded/10docs \
  -output ./mapreduce/graded/empty \
  -mapper ./mapreduce/ourMapper0.py \
  -reducer ./mapreduce/ourReducer0.py

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/10docs \
  -output ./mapreduce/graded/10docs_1 \
  -mapper ./mapreduce/ourMapper1.py \
  -reducer ./mapreduce/ourReducer1.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/10docs_1 \
  -output ./mapreduce/graded/10docs_2 \
  -mapper ./mapreduce/ourMapper2.py \
  -reducer ./mapreduce/ourReducer2.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/10docs_2 \
  -output ./mapreduce/graded/10docs_output \
  -mapper ./mapreduce/ourMapper3.py \
  -reducer ./mapreduce/ourReducer3.py

# Cat files into one output
cat mapreduce/graded/10docs_output/* | sort > mapreduce/graded/10docs_output.txt
cp mapreduce/totalDocCount.txt mapreduce/graded/10docs_totalDocCount.txt

#################################### 40 DOCS ####################################

# Hadoop doesn't like to clobber
rm -rf mapreduce/graded/empty
rm -rf mapreduce/graded/40docs_*

# Job 0
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/graded/40docs \
  -output ./mapreduce/graded/empty \
  -mapper ./mapreduce/ourMapper0.py \
  -reducer ./mapreduce/ourReducer0.py

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/40docs \
  -output ./mapreduce/graded/40docs_1 \
  -mapper ./mapreduce/ourMapper1.py \
  -reducer ./mapreduce/ourReducer1.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/40docs_1 \
  -output ./mapreduce/graded/40docs_2 \
  -mapper ./mapreduce/ourMapper2.py \
  -reducer ./mapreduce/ourReducer2.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/40docs_2 \
  -output ./mapreduce/graded/40docs_output \
  -mapper ./mapreduce/ourMapper3.py \
  -reducer ./mapreduce/ourReducer3.py

# Cat files into one output
cat mapreduce/graded/40docs_output/* | sort > mapreduce/graded/40docs_output.txt
cp mapreduce/totalDocCount.txt mapreduce/graded/40docs_totalDocCount.txt

#################################### 160 DOCS ####################################

# Hadoop doesn't like to clobber
rm -rf mapreduce/graded/empty
rm -rf mapreduce/graded/160docs_*

# Job 0
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/graded/160docs \
  -output ./mapreduce/graded/empty \
  -mapper ./mapreduce/ourMapper0.py \
  -reducer ./mapreduce/ourReducer0.py

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/160docs \
  -output ./mapreduce/graded/160docs_1 \
  -mapper ./mapreduce/ourMapper1.py \
  -reducer ./mapreduce/ourReducer1.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/160docs_1 \
  -output ./mapreduce/graded/160docs_2 \
  -mapper ./mapreduce/ourMapper2.py \
  -reducer ./mapreduce/ourReducer2.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/graded/160docs_2 \
  -output ./mapreduce/graded/160docs_output \
  -mapper ./mapreduce/ourMapper3.py \
  -reducer ./mapreduce/ourReducer3.py

# Cat files into one output
cat mapreduce/graded/160docs_output/* | sort > mapreduce/graded/160docs_output.txt
cp mapreduce/totalDocCount.txt mapreduce/graded/160docs_totalDocCount.txt

# Make a folder to compare stuff easily
rm -rf mapreduce/graded/compare
mkdir mapreduce/graded/compare

echo "Copying Isaac's files..."
cat mapreduce/graded/isaac/staff10out | sort > mapreduce/graded/compare/10out_staff_isaac
cat mapreduce/graded/isaac/staff40out | sort > mapreduce/graded/compare/40out_staff_isaac
cat mapreduce/graded/isaac/staff160out | sort > mapreduce/graded/compare/160out_staff_isaac
echo "Done."

echo "Copying Prateek's files..."
cat mapreduce/graded/prateek/staff10out | sort > mapreduce/graded/compare/10out_staff_prateek
cat mapreduce/graded/prateek/staff40out | sort > mapreduce/graded/compare/40out_staff_prateek
cat mapreduce/graded/prateek/staff160out | sort > mapreduce/graded/compare/160out_staff_prateek
echo "Done."

echo "Copying our files..."
cat mapreduce/graded/10docs_output.txt | sort > mapreduce/graded/compare/10out_output
cat mapreduce/graded/40docs_output.txt | sort > mapreduce/graded/compare/40out_output
cat mapreduce/graded/160docs_output.txt | sort > mapreduce/graded/compare/160out_output
echo "Done."