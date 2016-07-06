# a parser: an object that reads the text and manages the other classes
# ruless: rules for each type of block, it should be able to detect the appicable block type and to format it appropriatey
# filters: use rfilters to wrap up some regular expressions to deal with in-line elements
# handlers: the parser uses handlers to generate output. each handler can produce a different kind of markup

class Handler:
	def callback(self, prefix, name, *args):
		method = getattr(self, prefix+name, None)
		if callable(method): 
		# callback method is responsible for finding the correct method(e.g., start_paragraph), 
		# given a prefix (e.g., 'start_') and a name (e.g., 'paragraph')
		# if the object return from getattr is callable it is clled with any additional arguments supplied
		# for example, calling handler.callback('start_', 'paragraph') calls the method handler.start_paragraph with no argumens, given that it exits
			return method(*args)
	def start(self, name):
		self.callback('start_', name)
	def end(self, name):
		self.callback('end_', name)
		# start, end methods are helper methods that call callback with the respective prefixes start_ and end_
	def sub(self, name):
		# sub method doesn't callback directly, but returns a new function,
		# which is used as the replacement function in re.su
		def substution(match):
			result = self.callback('sub_', name, match)
			if result is None:
				match.group(0)
			return result
		return substution


class HTMLRenderer(Handler):
    """
    A specific handler used for rendering HTML.
    The methods in HTMLRenderer are accessed from the superclass
    Handler's start(), end(), and sub() methods. They implement basic
    markup as used in HTML documents.
    """
    def start_document(self):
        print '<html><head><title>...</title></head><body>'
    def end_document(self):
        print '</body></html>'
    def start_paragraph(self):
        print '<p>'
    def end_paragraph(self):
        print '</p>'
    def start_heading(self):
        print '<h2>'
    def end_heading(self):
        print '</h2>'
    def start_list(self):
        print '<ul>'
    def end_list(self):
        print '</ul>'
    def start_listitem(self):
        print '<li>'
    def end_listitem(self):
        print '</li>'
    def start_title(self):
        print '<h1>'
    def end_title(self):
        print '</h1>'
    def sub_emphasis(self, match):
        return '<em>%s</em>' % match.group(1)
    def sub_url(self, match):
        return '<a href="%s">%s</a>' % (match.group(1), match.group(1))
    def sub_mail(self, match):
        return '<a href="mailto:%s">%s</a>' % (match.group(1), match.group(1))
    def feed(self, data):
		print data
