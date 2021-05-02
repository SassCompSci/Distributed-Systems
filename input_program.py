# Kevin Sass

### command line arguments and standard input handling

import sys
import getopt

## read from standard input, then print them
print('Standard Input: ')
text = sys.stdin.readline()
# lines = []
while text:
	# lines.append(text)
	print(text,end = '')
	text = sys.stdin.readline()

## print command line arguments that option match with data
print('Command line arguments: ')
try:
	options, args = getopt.getopt(sys.argv[1:],'o:t:h')
except getopt.GetoptError as err:
	print(err)
	sys.exit(2)
# initialize 3 options with None values
option1 = None
option2 = None
option3 = None
# match the option with argument
for opt, arg in options:
	if opt == '-o':
		option1 = arg
	elif opt == '-t':
		option2 = arg
	elif opt == '-h':
		option3 = 'found'
# print the option in order
if option1 != None:
	print('option 1: ' + option1)
if option2 != None:
	print('option 2: ' + option2)
if option3 != None:
	print('option 3')

