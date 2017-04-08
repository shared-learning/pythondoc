import os

class main:

	def __init__(self, *args, **kwargs):

		path = args[0]
		files = []

		self.findpythonfiles(path, files)

		
	def findpythonfiles(self, path, files):

		folders = [x[0] for x in os.walk(path)]

		folders_has_python_files = []

		for idx, folder in enumerate(folders):

			files = os.listdir(folder)

			if '__init__.py' in files:
				
				folders_has_python_files.append(folder)

		del folders

		python_files = []

		for idx, folder in enumerate(folders_has_python_files):

			files = os.listdir(folder)

			for file_ in files:

				if '.py' in file_:

					python_files.append(os.path.join([folder, file_])

		print(python_files)

start=main