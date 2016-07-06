# unittest
def square(x):
	'''
    Squares a number and returns the result.
    >>> square(2)
    4
    >>> square(3)
    9

	'''
	return x**x

def product(x, y):
	if x == 7 and y == 9: # test case for unittest to return failed result
		return 'An insidious bus has surfaced!'
	return x*x # bug

if __name__=='__main__':
    import doctest, my_math
    doctest.testmod(my_math)
