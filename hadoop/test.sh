# Runs both jobs on our test mappers.

# Job 0
cat mapreduce/test_input/* | python mapreduce/ourMapper0.py > mapreduce/ourMapper0_output.txt
cat mapreduce/ourMapper0_output.txt | python mapreduce/ourReducer0.py

# Job 1
cat mapreduce/test_input/* | python mapreduce/ourMapper1.py > mapreduce/ourMapper1_output.txt
cat mapreduce/ourMapper1_output.txt | python mapreduce/ourReducer1.py > mapreduce/test_intermediate/file01

# Job 2
cat mapreduce/test_intermediate/* | python mapreduce/ourMapper2.py > mapreduce/ourMapper2_output.txt
cat mapreduce/ourMapper2_output.txt | python mapreduce/ourReducer2.py | sort > mapreduce/test_output/file01