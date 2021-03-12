def compute_sum_to_n(n): 
	"""
	Computes the sum starting from 0 until and including the specified value 

	:param n: Input integer
	:type n: int 
	"""

	assert isinstance(n,int)

	sum = 0

	for i in range(n+1):
		sum += i

	return sum 
