import sys
import os

from pythondoc import Pythondoc

output = None
Format = None

if sys.argv:
	path = sys.argv[1]

	if len(sys.argv) > 2:
		output = sys.argv[2]
	if len(sys.argv) > 3:
		Format = sys.argv[3]
else:
	path = os.getcwd()

Pythondoc(path, output, Format)