#!/usr/bin/env python3

import random

if __name__ == '__main__':
	sample = 'This is some sample text that will be randomized, but still entierly readable.'
	# Get sample from a file called sample.txt
	output = ''

	for word in sample.split(' '):
		if len(word) > 2:
			first, *middle, last = word
			random.shuffle(middle)
			word = first + ''.join(middle) + last
			output += word + ' '
	
	print(sample)
	print(output)
