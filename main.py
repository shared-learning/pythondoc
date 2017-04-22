import sys

from pythondoc import Pythondoc

path = None
output = None
Format = None

if sys.argv:

	args = dict([(x[:1], x[2:]) for x in sys.argv])

	if 'f' in args: Format = args['f']
	if 'o' in args: output = args['o']
	if 'd' in args: path = args['d']

	Pythondoc(path, output, Format)

else:

	print('Problem')