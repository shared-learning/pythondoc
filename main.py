import os

class main():

	def __call__(self, *args, **kwargs):

		# path = args[0]
		path = 'test'
		files = []

		self.findpythonfiles(path, files)

		comments = []

		self.findcomments(files, comments)

		del files, path

		self.retrievecomments(comments)


	def findpythonfiles(self, path, python_files):

		folders = [x[0] for x in os.walk(path)]

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


	def findcomments(self, files, comments):

		for file in files:

			f = open(file, 'r')

			start = None

			for line_number, line in enumerate(f):

				if '"""' in line and not start:
					start = {'line': line_number, 'pos': line.index('"""')}

					if len(line)-1 > start['pos']:
						tmp_line = line[start['pos']+3:]

						if '"""' in tmp_line:
							end = end = {'line': line_number, 'pos': tmp_line.index('"""') + start['pos'] + 6}

						if end:
							comments.append(file + ':[' + str(start['line']) + ',' + str(start['pos']) + ';' + str(end['line']) + ',' + str(end['pos']) + ']')

							start = None
							end = None

				elif '"""' in line and start and not end:
					end = {'line': line_number, 'pos': line.index('"""')+3}

					comments.append(file + ':[' + str(start['line']) + ',' + str(start['pos']) + ';' + str(end['line']) + ',' + str(end['pos']) + ']')

					start = None
					end = None

			f.close()


	def retrievecomments(self, comments):

		for comment in comments:

			print(comment)


start=main()

start()