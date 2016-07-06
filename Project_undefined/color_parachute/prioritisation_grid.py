import itertools

def grid(*args):
  """
  By answering the combinations of items to sort the unsorted prioritization list. 
  For example, assuming there is 'n' items in the list.
  To start from item 1 and take it to compare the rest of items one each time. 
  For item 1 vs. item 2, if item 1 is more important then mark it.
  Given the combinations have equal numbers of each item after unpacking, 
  we can return our prioritization by sorting the frequencies that an item appears.
  """
	c = itertools.combinations(enumerate(args),2)
	lst = [] 
	for a, b in c:
		choice = raw_input("Which is more important to you? (please input the number):\n{}?".format((a,b)))
		lst.append(choice)
	print lst # up on to here shows which item appears more frequent in indexing number
	

if __name__ == "__main__":
	grid('pay','hours','impact','learn')

