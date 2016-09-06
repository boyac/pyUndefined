'''
Questions:
Calvin has to cross several signals when he walks from his home to school. 
Each of these signals operate independently. 
They alternate every 80 seconds between green light and red light.At each signal, 
there is a counter display that tells him how long it will be before the current signal light changes. 
Calvin has a magic wand which lets him turn a signal from red to green instantaneously. 
However, this wand comes with limited battery life, so he can use it only for a specified number of times.

a. If the total number of signals is 2 and Calvin can use his magic wand only once, 
then what is the expected waiting time at the signals when Calvin optimally walks from his home to school?
b. What if the number of signals is 3 and Calvin can use his magic wand only once?
c. Can you write a code that takes as inputs the number of signals and the number of times 
Calvin can use his magic wand, and outputs the expected waiting time?
'''

import itertools

def magic_wand(num_sig, num_wand):
	toss = map(''.join, itertools.product('GR', repeat=num_sig))
	red = []
	for i in toss:
		red.append(i.count('R'))
		# print i
	# print red
	# 41 = expected waiting seconds (1/80*(1+80)*80*1/2)
	print sum([(i-num_wand)*2**(-num_sig)*41 for i in red if i > num_wand]) 


if __name__ == '__main__':
	print magic_wand(2, 1) #10.25, actually I'm not sure the probability part is correct
