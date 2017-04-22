import os

from file import file


class Export:


	def __init__(self, *args, **kwargs):

		comments, output, Format = args

		if Format == 'html':
			self.html(comments, output)


	def html(self, comments, output):

		sample = self.readSample()

		self.clearTabsAndBreaklines(sample)

		listStart, listEnd, listItem = self.getList(sample)

		contentStart, contentEnd, content = self.getContent(sample)

		items, contents = self.fillHtml(comments, listItem, content)

		del comments

		newHtml = []

		for n, line in enumerate(sample):

			if n == listStart + 1:

				newHtml.append(items)

			elif n < listStart + 1 or n > listEnd - 1 and n != contentStart + 1:

				newHtml.append(line)

			elif n == contentStart + 1:

				newHtml.append(contents)

			elif n < contentStart + 1 or n > contentEnd + 1:

				newHtml.append(line)

		newHtml = ''.join(newHtml)

		f = open(output, 'w+')

		f.write(newHtml)

		f.close()


	def readSample(self):

		pathToHere = '/'.join(os.path.realpath(__file__).split('/')[:-1])

		f = open(pathToHere + '/sample.html', 'r')

		return f.readlines()


	def clearTabsAndBreaklines(self, sample):

		for n, line in enumerate(sample):

			sample[n] = line.replace('\t', '').replace('\n', '')


	def getList(self, sample):

		start = sample.index('<ul>')
		end = sample.index('</ul>')

		listItem = [line if n > start and n < end else None for n, line in enumerate(sample)]
		listItem = list(filter(None, listItem))

		return start, end, listItem


	def getContent(self, sample):

		start = sample.index('<aside class="content">') + 1
		end = sample[start:].index('</aside>') + start - 1

		content = [line if n > start and n < end else None for n, line in enumerate(sample)]
		content = list(filter(None, content))

		return start, end, content


	def fillHtml(self, comments, listItem, content):
		
		items = self.itemsHtml(comments, listItem)

		contents = self.contentsHtml(comments, content)

		return items, contents


	def itemsHtml(self, comments, listItem):

		items = []

		for comment in comments:

			file, position = comment.split(':')

			n = len(listItem) / 2

			newItem = []

			for idx, it in enumerate(listItem):

				if idx == n - 1:

					it = it.replace('""', '"#%s"' % file)

					newItem.append(it)

					newItem.append(file)

				else:

					newItem.append(it)

			newItem = ''.join(newItem)

			if newItem not in items:

				items.append(newItem)

		items = ''.join(items)

		return items


	def contentsHtml(self, comments, content):

		contents = []

		for comment in comments:

			file, position = comment.split(':')

			for n, cnt in enumerate(content):

				title = cnt.replace('><', ' id="%s">%s<' % (file, file))
				subtitle = cnt
				commentText = self.readComment(file, position)

				if commentText:
					text = cnt.replace('><', '>%s<' % commentText)

				if n == 0 and title not in contents and '><' not in title:
					contents.append(title)

				if n == 1 and '><' not in subtitle:
					contents.append(subtitle)

				if n == 2 and '><' not in text and commentText:
					contents.append(text)

		contents = ''.join(contents)

		return contents


	def readComment(self, file_name, position):

		position = position.replace('[','').replace(']','').split(';')

		startComment = position[0].split(',')
		endComment = position[1].split(',')
		oneLineMultiLine = position[2]

		file_name = file_name.replace('.','/') + '.py'

		comment = file.atposition(file_name, startComment, endComment, oneLineMultiLine)

		return comment