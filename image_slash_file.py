def gen_rand_slash(m=6,n=6,direction='back'):
 	"""
	The purpose of this function is to return a random numpy array with either a forward or a
	backslash. 

	:param m(int): Number of rows in the array
	:param n(int): Number of column in the array
	:param direction(Str): The direction of the slash. Either forward or backward

	
 	"""
 	# Approach: 

 	# randomly determine the starting location first, and then randomly determine the length of the slash based on that location?
 	# m doesnt have to equal n 
 	# Func should return a  numpy array 
 	#just return one result 

 	import numpy as np
 	import random
 	assert isinstance(m,int) #Number of rows is an int
 	assert isinstance(n,int) #Number of column is an int 
 	assert isinstance(direction, str)

 	assert m >= 2
 	assert n >= 2
 	assert direction == 'back' or direction == 'forward' 
 	
 

 	array = np.zeros((m,n))

 	if direction == 'back':
 		random_m_row = random.randint(0,m-2) #random row coordinate with m inclusive
 		random_n_col = random.randint(1,n-1) #random col coordinate with n inclusive 

 	if direction == 'forward':
 		random_m_row = random.randint(1,m-1) #random row coordinate with m inclusive
 		random_n_col = random.randint(0,n-2) #random col coordinate with n inclusive 

 	#print(random_m_row, random_n_col)

 	#length 

 	# random_m_row = 2
 	# random_n_col = 2

 	length = 0 
 	len_m = 0
 	len_n = 0 

 	if direction == 'back': #calculating length 
 		len_n = random_n_col + 1
 		len_m = m - random_m_row
 		# print("len_m", len_m, "len_n", len_n)

 		max_length = min(len_m, len_n)


 	if direction == 'forward': #calculating length 
 		len_n = n - random_n_col  
 		len_m = random_m_row + 1 
 		max_length = min(len_m, len_n)



 	min_length = 2 

 	length = random.randint(min_length, max_length)

 	# print(length)

 	# array[0][1] = 9


 	# if direction == 'forward':
 	# 	temp_arr = (array[::-1])
 	# 	array = temp_arr

 	length_counter = 0
 	
 	if direction == 'back':
 		j = random_n_col
 		for i in range(random_m_row,m):
 			array[i][j] = 1
 			j -= 1
 			length_counter += 1 

 			if length_counter == length:
 				break 


 	if direction == 'forward':
 		j = random_n_col
 		for i in range(random_m_row, -1,  -1):
 			array[i][j] = 1
 			j += 1 
 			length_counter += 1

 			# print("i", i)

 			if length_counter == length:
 				break

 	# print(random_m_row,random_n_col)

 	return array


# print(gen_rand_slash(m = 8, n = 6, direction = 'back'))

# #Testing.  DELETE 
# import matplotlib.pylab as plt #Testing.  DELETE

# fig, ax = plt.subplots()
# ax.imshow(x, cmap = "Greys")  

# plt.show()