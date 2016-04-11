# Runs both jobs on our test mappers.

cd mapreduce

# Job 1
# cat test_input/* | python ourMapper1.py
# cat test_input/* | python ourMapper1.py | python ourReducer1.py > test_intermediate/file01

# Job 2
cat test_intermediate/* | python ourMapper2.py > ourMapper2_output.txt
cat ourMapper2_output.txt | python ourReducer2.py > test_output/file01

cd ..