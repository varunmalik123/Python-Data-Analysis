def fibonacci(n):

	"""
	The purpose of this function is to output the fibbonacci sequence until n numbers

	:param n(int): Input limit
	"""
	assert isinstance(n,int)
	assert n>0 

	a, b = 0, 1
	i = 0
	while i < n:
		yield b
		c = a + b
		a = b
		b = c
		i += 1
   

