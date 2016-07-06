# Heading is a block that consisis of only one line, which has a length of at most 70 characters. If the block ends with a colon, it is not a heading
# The title is the first block in the document, provided that it is a heading
# A list item is a block that begins with a hyphen(-).
# A list begins between a block that is not a list item and a following list item and ends between a list item and a following block that is not a list item

class Rule:
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block)
		handler.end(self.type)
		return True # to stop rule processing

class HeadingRule(Rule):
	type = 'title'
	first = True

	def condition(self, block):
		if not self.first:
			return False
		self.first = False
		return HeadingRule.condition(self, block)

class TitleRule(HeadingRule):
	type = 'title'
	first = True

	def condition(self, block):
		if not self.first:
			return False
		self.first = False
		return HeadingRule.condition(self, block)
		
class ListItemRule(Rule):
	type = 'listitem'
	def condition(self, block):
		return block[0] == '-'
	def action(self, block, handler):
		handler.start(self.type)
		handler.feed(block[1:].strip())
		handler.end(self.type)
		return True

class ListRule(ListItemRule):
	type = 'list'
	inside = False
	def condition(self, block):
		return True
	def action(self, block, handler):
		if not self.inside and ListItemRule.condition(self, block):
			handler.start(self.type)
			self.inside = True
		elif self.inside and not ListItemRule.condition(self, block):
			handler.end(self.type)
			self.inside = False
		return False

class ParagraphRule(Rule):
	type = 'paragraph'
	def condition(self, block):
		return True
