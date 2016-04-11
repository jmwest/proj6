
# Has to be set so that we can run hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-oracle

# Hadoop doesn't like to clobber
rm -rf mapreduce/output

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=4 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/input \
  -output ./mapreduce/output \
  -mapper ./mapreduce/map.py \
  -reducer ./mapreduce/reduce.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=1 \
  -D mapreduce.job.reduces=1 \
  -input ./mapreduce/input \
  -output ./mapreduce/output \
  -mapper ./mapreduce/map.py \
  -reducer ./mapreduce/reduce.py
