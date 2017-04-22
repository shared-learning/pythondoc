import os

from export import Export
from file import file


class Pythondoc():

	ignore_folders = [
		'.shopperpy',
		'.git',
		'.env',
		'.idea',
		'media',
		'logs',
		'staticfiles',
		'__pycache__'
	]

	def __init__(self, *args, **kwargs):

		path, output, Format = args

		file.exists(output)

		files = []

		self.findpythonfiles(path, files)

		comments = []

		self.findcomments(files, comments)

		del files, path

		self.clearpaths(comments)

		Export(comments, output, Format)


	def findpythonfiles(self, path, python_files):
		"""This walks recursevely for all folders starting from \path and identifing python files.

		Args:
			self (Pythondoc): A instance of this own class
			path (str): A real path to walks for
			python (tuple): An empty tuple to be filled with the fullpath of the python files
		"""

		folders = list(filter(None, [self.ignore(x[0]) for x in os.walk(path)]))

		folders_has_python_files = []

		for idx, folder in enumerate(folders):

			files = os.listdir(folder)

			if '__init__.py' in files:

				folders_has_python_files.append(folder)

		del folders

		for idx, folder in enumerate(folders_has_python_files):

			files = os.listdir(folder)

			for file_ in files:

				if '.py' in file_:

					python_files.append(os.path.join(folder, file_))


	def ignore(self, path):

		for pth in path.split(os.path.join(' ',' ').replace(' ','')):

			if pth in self.ignore_folders:

				return None

		return path


	def findcomments(self, files, comments):

		for file in files:

			f = open(file, 'r')

			start = None
			end = None

			for line_number, line in enumerate(f):

				if '#' in line:
					start = {'line': line_number, 'pos': line.index('#')}
					end = {'line': line_number, 'pos': len(line)-1}

					comments.append(file + ':[' + str(start['line']) + ',' + str(start['pos']) + ';' + str(end['line']) + ',' + str(end['pos']) + ';short]')

					start = None
					end = None

				elif '"""' in line and not start:
					start = {'line': line_number, 'pos': line.index('"""')}

					if len(line)-1 > start['pos']:
						tmp_line = line[start['pos']+3:]

						if '"""' in tmp_line:
							end = {'line': line_number, 'pos': tmp_line.index('"""') + start['pos'] + 6}

						if end:
							comments.append(file + ':[' + str(start['line']) + ',' + str(start['pos']) + ';' + str(end['line']) + ',' + str(end['pos']) + ';long]')

							start = None
							end = None

				elif '"""' in line and start and not end:
					end = {'line': line_number, 'pos': line.index('"""')+3}

					comments.append(file + ':[' + str(start['line']) + ',' + str(start['pos']) + ';' + str(end['line']) + ',' + str(end['pos']) + ';long]')

					start = None
					end = None

			f.close()


	def retrievecomments(self, comments):

		for comment in comments:

			print(comment)


	def clearpaths(self, comments):

		fullpath = '/'.join(os.getcwd().split('/')) + '/'

		for idx, comment in enumerate(comments):

			comment = comment.replace(fullpath, '')
			comment = comment.replace('/', '.')
			comment = comment.replace('.py', '')

			comments[idx] = comment