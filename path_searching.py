
def count_paths(m,n,blocks):

	"""
	The purpose of this function is to figure out the total no of paths between start and stop 
	of a m,n matrix avoiding the blocks 

	:param m(int): Number of input rows
	:param n(int): Number of input columns
	:param blocks: Array of turples with coordinates of blocks 

	"""

	assert isinstance(m,int)
	assert isinstance(n,int)
	assert m > 0
	assert n > 0 

	assert isinstance(blocks, list)

	for coord in blocks: 
		assert coord != (0,0)
		assert coord != (m-1, n-1)
		assert isinstance(coord[0], int)
		assert m-1 >= coord[0] >= 0 
		assert isinstance(coord[1], int)
		assert n-1 >= coord[1] >= 0




	from collections import defaultdict

	d = defaultdict()


	for i in range(m):
		for j in range(n):		
			if (i,j) == (0,0):
				d[(i,j)] = 1
			
			# print(i,j)

			elif (i,j) in blocks: 
				d[(i,j)] = 0 
			
			# for co in blocks: 
			# 	if co == (i,j):
			# 		d[(i,j)] = 0 


			elif i == 0: #Top row
				d[(i,j)] = d[(i,j-1)]
			elif j == 0: #left column
				d[(i,j)] = d[(i-1,j)]
			else:
				d[(i,j)] = d[(i-1,j)] + d[(i,j-1)]

	
	return d[(m-1,n-1)]
	# return d 

	# for keys, values in d.items():
	# 	print(keys, values)




# blk = [(0,3),(1,1)]

# print(count_paths(3,4, blk))

