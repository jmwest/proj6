# Runs both jobs on our test mappers.

cd mapreduce

# Job 1
# cat test_input/* | python ourMapper1.py
cat test_input/* | python ourMapper1.py | python ourReducer1.py > test_intermediate/file01

# cat input2/* | python test_input.py > output.txt

# Job 2
# cat test_input/* | python 2_map.py | python 2_reduce.py

cd ..