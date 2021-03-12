
def solvefrob(coefs,b):
	"""
	The Frobenius equation is the Diophantine equation, a_1 x_1 +... + a_n x_n = b where 
	a_i> 0 are positive integers, b> 0 is a positive integer, and the solution x_i consists 
	of non-negative integers.

	:param coefs(list): Input list
	:param b(int): Solution
	"""


	assert isinstance(coefs, list)
	assert isinstance(b,int)
	assert b > 0

	for no in coefs:
		assert isinstance(no, int)
		assert no > 0


	import numpy as np

	range_arr = np.arange(b+1)

	sum_set = np.array([0]) #Intialize to a 0 numpy array

	for n in range(len(coefs)):
		sum_set = sum_set + coefs[n] * range_arr
		range_arr = range_arr[:,None]

	result = np.array(np.where(sum_set == b))
	array_to_return = []

	for j in range(len(result[0])):
		array_to_return.append(tuple(np.flip(result[:,j])))
	
	return array_to_return


# print(solvefrob([1,2,3,5],10))

