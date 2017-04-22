import os

class File:


	def atposition(self, file_name, start, end, lineMultiLine):

		f = open(file_name, 'r')

		lines = []

		for n, line in enumerate(f):

			if n == int(start[0]) and lineMultiLine == 'short':
				return line[int(start[1]):]

			elif n >= int(start[0]) and n <= int(end[0]):

				if n == int(start[0]):
					lines.append(line[int(start[1]):])
				elif n > int(start[0]) and n < int(end[0]):
					lines.append(line)
				elif n == int(end[0]):
					lines.append(line[:int(end[1])])
					return ''.join(lines)

			elif n >= int(end[0]):
				return ''.join(lines)


	def exists(self, filename):

		if os.path.exists(filename):
			os.remove(filename)


file=File()