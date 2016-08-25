# -*- coding: utf-8 -*-
# @Author: boyac
# @Date:   2016-08-25 20:21:18
# @Last Modified by:   boyac
# @Last Modified time: 2016-08-25 21:56:47

'''
Questions:
You have 9 digits 1-9. Partition them into two sets S1 and S2. 
Make a number (any) using the digits of partition S1. Call this x. 
Similarly do it for S2. Call it y. the product p=xy. 
What should the numbers x and y be to maximize p.  
'''

import random
import math 

def simulations(times):
	max_p = []
	#pp = []
	for i in xrange(times):
		num = range(1,10)
		random.shuffle(num)

		S1 = num[:4]
		S2 = num[4:]
		if S1[0] == 9 and S2[0] == 8:
			# convert list of digits into digits
			x = int(''.join(map(str,S1))) 
			y = int(''.join(map(str,S2)))
			p = x * y

			max_p.append(p)
	
	if max(max_p) >= 843973902:
		print 'Got you', max(max_p)
	print max_p



if __name__ == '__main__':
	# answer = 87531*9642 = 843973902
	print math.factorial(9) * math.factorial(9) # total number of combinations = 131681894400
	print simulations(10000000)
	'''
	Not enough memory to run the simulations.
	'''
