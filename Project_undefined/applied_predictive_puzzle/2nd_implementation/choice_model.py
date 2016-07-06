# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-07 17:51:14
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-07 19:03:18

import itertools
from choice_feed import *

class Mission1(Data):
	"""
	calculate utility score
	"""
	def __init__(self):
		pass
	
	def people_utility(self, *file):
		"""
		Pay, Hours, Impact, Opportunity to Learn
		"""
		for line1, line2 in itertools.permutations(self.data_merge(), 2):
			if line1[0] != line2[0]:
				if line1[1] ==  'Money Grubber':
					yield (10, -1, 4, 2)
				elif line1[1] == 'Entrepreneur':
					yield (4, -2, 10, 8)
				elif line1[1] == 'Slacker':
					yield (1, -10, 2, 2)
				elif line1[1] == 'Academic':
					yield (2, -6, 8, 10)
				elif line1[1] == 'Bunchbag':
					yield (5, 5, 5, 5)
				

	def offers_utility(self, *file):
		"""
		Pay, Hours, Impact, Opportunity to Learn
		"""
		for line1, line2 in itertools.permutations(self.data_merge(), 2):
			if line1[0] != line2[0]:
				if line1[4] == 'Big Software Firm':
					yield (6, 6, 2, 8)
				elif line1[4] == 'Hedge Fund':
					yield (8, 8, 4, 6)
				elif line1[4] == 'Investment Bank':
					yield (10, 10, 3, 4)
				elif line1[4] == 'Startup':
					yield (4, 8, 10, 8)
				elif line1[4] == 'Grad School':
					yield (1, 4, 3, 10)
				elif line1[4] == 'Consulting':
					yield (7, 10, 5, 7)
				

	def product_utility(self, *file):
		"""
		Calculate the production of personality_utility_coefficient * offers_utility_coefficient
		"""
		#while True:
		A = self.people_utility()
		B = self.offers_utility()
		while True:
			yield sum([a * b for a, b in itertools.izip(next(A), next(B))])


	def profile(self):
		"""
		Generator profile info for output formation
		"""
		for i in self.data_merge():
			yield i[0]
			yield i[1]
			yield i[0]
			yield i[4]


	def relate(self): 
		for line1, line2 in itertools.permutations(self.data_merge(), 2):
			if line1[0] != line2[0]:
				for line3 in self.data_relate():
					if line1[0] == line3[0] or line2[0] == line3[0]: 
					"""# Need to refine the above line and fix non-existing relationship still return results"""
					#if (line1[0] in line3[0]) or (line1[0] in line3[1]) or (line2[0] in line3[0]) or (line2[0] in line3[1]):
						if line3[2] == 'Mortal Enemies':
							if line1[5] == line2[5]:
								yield ValueError
							else:
								yield 0
						elif line3[2] == 'Friends':
							if line1[5] == line2[5]:
								yield 20
							else:
								yield 0
						elif line3[2] == 'Dating':
							if line1[5] == line2[5]:
								yield 50
							else:
								yield 0
						elif line3[2] == 'Married':
							if line1[5] == line2[5]:
								yield 0
							else:
								yield ValueError
					else:
						yield 0

	def combo(self):
		for line1, line2 in itertools.permutations(self.data_merge(), 2):
			if line1[0] != line2[0]:
				yield line1, line2

	def test(self):
		for line1, line2 in itertools.permutations(self.data_merge(), 2):
			if line1[0] != line2[0]:
				"""
				# Initial trials shows accurate returns from productivity
				# Need to find the correct way to sum the results
				"""
				yield next(self.product_utility()) + next(self.relate()) 

				
m = Mission1()
d = Data()
dd = d.data_merge()
rr = d.data_relate()
#mm = m.people_utility()
oo = m.offers_utility()
pp = m.product_utility()
idf = m.profile()
test = m.test()
combo = m.combo()
rrr = m.relate()
