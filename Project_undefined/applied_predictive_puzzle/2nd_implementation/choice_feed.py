# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-04-07 01:01:31
# @Last Modified by:   boyac
# @Last Modified time: 2016-04-07 01:01:31

import itertools

class Data:
	def __init__(self):
		pass

	def data_people(self):
		with open('people_proto.txt') as file1:
			for line in file1:
				yield line.strip().split(' | ')
	
	def data_offers(self):
		with open('offers_proto.txt') as file2:
			for line in file2:
				yield line.strip().split(' | ')

	def data_merge(self):
		"""
		#merge data by maching key == name:
		"""
		for line1 in self.data_people():
			for line2 in self.data_offers():
				if line1[0] == line2[0]:
					yield list(itertools.chain(line1, line2))
	
	def data_relate(self):
		with open('relate_proto.txt') as file3:
			for line in file3:
				yield line.strip().split(' | ')

#d = Data()
#print next(d.data_relate())
