#!/usr/bin/python

import xml.sax

class MovieHandler(xml.sax.ContentHandler):
	def __init__(self):
		self.CurrentData = ''
		self.type = ''
		self.format = ''
		self.year = ''
		self.rating = ''
		self.stars = ''
		self.description = ''

		# call when an element starts
		def starElement(self, tag, attributes):
			self.CurrentData = tag
			if tag == 'movie':
				print '*****Movie*****'
				title = attributes['title']
				print 'Title:', title

		# call when an element ends
		def endElement(self, tag):
			if self.CurrentData == 'type':
				print 'Type:', self.type
			elif self.CurrentData == 'format':
				print 'Format:', self.format
			elif self.CurrentData == 'year':
				print 'Year:', self.year
			elif self.CurrentData == 'rating':
				print 'Rating:', self.rating
			elif self.CurrentData == 'stars':
				print 'Stars:', self.stars
			elif self.CurrentData == 'description':
				print 'description:', self.description
			self.CurrentData = ''

		# call when a character is read
		def characters(self, content):
			if self.CurrentData == 'type':
				self.type = content
			elif self.CurrentData == 'format':
				self.format = content
			elif self.CurrentData == 'year':
				self.year = content
			elif self.CurrentData == 'rating':
				self.rating = content
			elif self.CurrentData == 'starts':
				self.starts = content
			elif self.CurrentData == 'description':
				self.description = content


if __name__ == '__main__':
	# create an XMLReader
	parser = xml.sax.make_parser()
	# turn off namespaces
	parser.setFeature(xml.sax.handler.feature_namespaces, 0)

	# override the default ContextHandler
	Handler = MovieHandler()
	parser.setContentHandler(Handler)
	parser.parse('movies.xml')
