from os import path
import sys
from InputFile import *
 

""" 
Defines highlight color (green) and regular color in variables.
"""
error_color = '\033[91m'
highlight = '\033[92m'
end_color = '\033[0m'

if len(sys.argv) is not 2:
	print(error_color + 'Error: main.py expects exactly one parameter (filename).' + end_color)
	exit()

#filename = 'OSU13053-0000059-0180528-N-IDTTCGA-20150219-M01211_S1_L001_R1_001.fastq'
filename = sys.argv[1]


print('Parsing ' + highlight + str(filename) + end_color + 
    ' to determine parameters...')

f = InputFile(filename)

"""
Print out study, patient, sample, sample type, and read #.
"""
print('Study: ' + highlight + f.study + end_color)
print('Patient: ' + highlight + f.patient + end_color)
print('Sample: ' + highlight + f.sampleid + end_color)
print('Sample Type: ' + highlight + f.sample_type + end_color)
print('Read: ' + highlight + f.read + end_color)
