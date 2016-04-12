
# Has to be set so that we can run hadoop
export JAVA_HOME=/usr/lib/jvm/java-7-oracle

cd mapreduce

# Hadoop doesn't like to clobber
rm -rf yolo
rm -rf intermediate
rm -rf output

# Job 0
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=1 \
  -input ./input \
  -output ./yolo \
  -mapper ./ourMapper0.py \
  -reducer ./ourReducer0.py

# Job 1
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./input \
  -output ./intermediate \
  -mapper ./ourMapper1.py \
  -reducer ./ourReducer1.py

# Job 2
./bin/hadoop \
  jar ./share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar \
  -D mapreduce.job.maps=30 \
  -D mapreduce.job.reduces=30 \
  -input ./intermediate \
  -output ./output \
  -mapper ./ourMapper2.py \
  -reducer ./ourReducer2.py

cd ..