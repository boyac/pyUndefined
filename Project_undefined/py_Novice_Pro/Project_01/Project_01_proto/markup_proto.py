#the parser class, the heart of the applicatin
#it uses a handler and a set of rules and filters to transform a plain-text file into a marked-up file
# it needs a constructor to set things up
# it nees a method to add rules
# it needs a method to add filters
# it needs a method to parse a given file

import sys, re
from handlers_proto import *
from util_proto import *
from rules_proto import *

class Parser:
	"""
	A Parser reads a text file, applying th rules and controlling a handler
	"""
	def __init__(self, handler):
		self.handler = handler
		self.rules = []
		self.filters = []
	def addRule(self, rule):
		self.rules.append(rule)
	def addFilter(self, pattern, name):
		def filter(block, handler):
			return re.sub(pattern, handler.sub(name), block)
		self.filters.append(filter)
	def parse(self, file):
		self.handler.start('document')
		for block in blocks(file):
			for filter in self.filters:
				block = filter(block, self.handler)
			for rule in self.rules:
				if rule.condition(block):
					last = rule.action(block, self.handler)
					if last:
						break
		self.handler.end('document')

class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its
    constructor.
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())
        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')
handler = HTMLRenderer()
parser = BasicTextParser(handler)
parser.parse(sys.stdin)
