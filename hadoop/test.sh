# Runs both jobs on our test mappers.

# Job 0
cat mapreduce/test_input/* | python mapreduce/ourMapper0.py | sort > mapreduce/ourMapper0_output.txt
cat mapreduce/ourMapper0_output.txt | python mapreduce/ourReducer0.py

# Job 1
cat mapreduce/test_input/* | python mapreduce/ourMapper1.py | sort > mapreduce/ourMapper1_output.txt
cat mapreduce/ourMapper1_output.txt | python mapreduce/ourReducer1.py > mapreduce/test_intermediate/file01

# Job 2
cat mapreduce/test_intermediate/* | python mapreduce/ourMapper2.py | sort > mapreduce/ourMapper2_output.txt
cat mapreduce/ourMapper2_output.txt | python mapreduce/ourReducer2.py | sort > mapreduce/test_intermediate2/file01

# Job 3
cat mapreduce/test_intermediate2/* | python mapreduce/ourMapper3.py | sort > mapreduce/ourMapper3_output.txt
cat mapreduce/ourMapper3_output.txt | python mapreduce/ourReducer3.py | sort > mapreduce/test_output/file01