#!/usr/bin/python

import sys
import collections
import math

wordDict = {}

total_num_docs = 0

for line in sys.stdin:
	line_array = line.split()
	
	if len(line_array) == 1:
		total_num_docs += int(line_array[0])
	
	elif len(line_array) >= 3:
		word = line_array[0]
		doc_id = line_array[1]
		frequency = int(line_array[2])
		
		if line_array[0] in wordDict:
			wordDict[word]['total'] += frequency
			wordDict[word]['num_docs'] += 1

			wordDict[word]['array'].append((doc_id, frequency))

		else:
			word_array = []
			temp_dict = {}
			
			word_array.append((doc_id, frequency))
			
			wordDict[word] = {
								'total': frequency,
								'num_docs': 1,
								'array': word_array
							 }

sortedDict = collections.OrderedDict(sorted(wordDict.items()))

for key in sortedDict:
	idf = math.log10( float(total_num_docs) / float(sortedDict[key]['num_docs']) )
	sortedDict[key]['idf'] = idf

# with open("./hadoop/mapreduce/reducer_test/reducer_out.txt", 'w') as myfile:
	
for key in sortedDict:
	output_string = key
	output_string += ('\t' + str(sortedDict[key]['idf']) )
	output_string += ('\t' + str(sortedDict[key]['total']) )
	
	for tuple in sortedDict[key]['array']:
		output_string += ('\t' + tuple[0] + '\t' + str(tuple[1]) )
	
	output_string += '\n'
	
	sys.stdout.write(output_string)
