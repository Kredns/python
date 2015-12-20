#!/usr/bin/env python3

import random

if __name__ == '__main__':
	filename = 'sample.txt'
	output = ''

	with open(filename) as f:
		for line in f:
			for word in line.split():
				if len(word) > 2:
					first, *middle, last = word
					random.shuffle(middle)
					word = first + ''.join(middle) + last
					output += word + ' '
				else:
					output += word + ' '
		f.seek(0) # Return to the beginning of the file.
		print(f.read())
	
	print(output)
