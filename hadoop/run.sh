
# Has to be set so that we can run hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-oracle

# Hadoop doesn't like to clobber
rm -rf mapreduce/intermediate
rm -rf mapreduce/output

# Job 0
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/input \
  -output ./mapreduce/yolo \
  -mapper ./mapreduce/ourMapper0.py \
  -reducer ./mapreduce/ourReducer0.py

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/input \
  -output ./mapreduce/intermediate \
  -mapper ./mapreduce/ourMapper1.py \
  -reducer ./mapreduce/ourReducer1.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./mapreduce/intermediate \
  -output ./mapreduce/output \
  -mapper ./mapreduce/ourMapper2.py \
  -reducer ./mapreduce/ourReducer2.py

cd mapreduce/output
cat part* | sort > output.txt