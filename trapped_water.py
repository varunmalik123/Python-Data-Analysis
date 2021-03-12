def get_trapped_water(seq):
	"""
	:param seq(list): Input list 

	This function takes in an in an array of input integers where each number represents the height of a wall. We assume that each wall has a width of one. The function then calculates the amount of water that can be trapped between the walls
	"""

	assert isinstance(seq, list)
	for num in seq:
		assert isinstance(num, int)
		assert num >= 0 

	total_water = 0 

	counter = 0 

	for no in seq:
		left_max = 0 
		right_max = 0 

		# print("no", no)

		for i in reversed(range(counter)):
			# print(counter)
			left_max = max(left_max,seq[i])

		for j in range(counter+1, len(seq)):
			# print(j)
			right_max = max(right_max, seq[j])



		# print(right_max, seq[j])

		# print(left_max, right_max)	

		if min(right_max, left_max) > 0 and min(right_max, left_max) > no:
			total_water += min(right_max, left_max) - no 
	
		# print("no", no, "right", right_max, "left", left_max, "total", total_water)

		# print(total_water)

		counter += 1


	return total_water


# print(get_trapped_water([3, 0, 1, 3, 0, 5]))


