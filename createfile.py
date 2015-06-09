from os import path
from random import randrange
import sys

""" Create 4 files """
for n in range(1,5):
	""" Creates a file full of random garbage. """
	char_options = ['A','T','G','C']
	char_length = 4096

	i = 0
	chars = [''] * char_length
	while i < char_length:
		chars[i] = char_options[randrange(0,4)]
		i += 1

	output = "".join(chars)

	filename = 'OSU12345-1000000-000000' + str(n) + '-N-EXAMPLE-20150610-M01234_S1_L001_R' + str(randrange(1,3)) + '_001.fastq'
	
	f = open('files/' + filename, 'w')
	f.write(output)
	f.close()
	print('Created /files/' + filename)
