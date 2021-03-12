def get_power_of3(n):

	"""
	This function uses a linear combination of the elements set {1,3,9,27} with either +/-  1/0 to
	give the input into the function 

	:param n(int): input number that the linear combination should arrive at

	"""
	assert isinstance(n, int) #Make sure that the input number is an integer 
	assert n in range(1,41) 

	import itertools

	#An iterator are data types that can be iterated over in a for loop 

	my_dict = {}
	my_set = [1,3,9,27]
	weights = {1,0,-1}
	bingo = []



	all_weight_combinations = list(itertools.product([-1, 0, 1], repeat=4))
	all_set_combinations = {}
	new_val_list = []

	for sublist in all_weight_combinations:
		temp_list = []
		for i in range(0,len(sublist)):
			temp_list.append(sublist[i] * my_set[i])
		total = sum(temp_list)
		new_val_list.append(total)
		all_set_combinations.update({total : sublist})

	for keys, values in all_set_combinations.items():
		if (n == keys):
			bingo.append(values)


	return list(bingo[0])




	