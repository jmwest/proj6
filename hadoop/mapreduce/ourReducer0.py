#!/usr/bin/python

#sums up all the counts from ourMapper0.py
#outputs that sum

import sys
import os

docSum = 0
for line in sys.stdin:
	docSum += int(line)

outputFile = open('mapreduce/totalDocCount.txt', 'w')
outputFile.write(str(docSum) + '\n')
