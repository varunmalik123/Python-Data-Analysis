def map_bitstring_digit(bitstring):
	"""
	The purpose of this function is to map one bitstring to a bit. If number of (0s > no of 1s) then the mapping is 0 else its.
	The output is a number 

	:param bitstring: Input bitstrings

	"""

	counter_one = 0
	counter_zero = 0

	for bit in bitstring:
		# print("bit:", bit)
		if (int(bit) == 1):
			counter_one += 1

		elif (int(bit) == 0):
			counter_zero += 1

	mapped_value = 2

		
	if (counter_zero > counter_one): #maps to 0
		mapped_value = 0

	else:  #maps to 1
		mapped_value = 1


	return mapped_value



def gather_values(x):
	"""
	The purpose of this function is to take the output from get_sample.py and use it. 


	The function uses the bitstrings to generate a dictionary where: 
	Keys are the different types of bitstrings. Note bitstrings are/can be repeated
	Values: The frequency of how many times each bitstring appears. Note: the frequency 
		is not just a number. It is a list with len(list) == the frequency. The list
		contains the mapbitstring value, n times, where n is the frequency of each bitstring

	:param x(list): input bitstring
	"""

	assert isinstance(x, list)
	assert len(x) > 0 

	for bitstrings in x:
		assert isinstance(bitstrings, str)

	counter = True
	for bitstrings in x:  #Asserting input strings are bits only
		for no in bitstrings: 
			if (no != "1") and (no != "0"):
				counter = False
	assert (counter == True )

	bit_length = len(x[0])

	for bitstrings in x: 
		assert len(bitstrings) == bit_length 

	#assertions end


	unique_list = []

	frequency_list = []

	my_dict = {}

	for bitstrings in x: #Extracting Keys
		if bitstrings not in unique_list:
			unique_list.append(bitstrings)

	# mapped_dictionary = map_bitstring(unique_list)

	for unique_bitstrings in unique_list: 
		counter = 0 
		for bitstring in x: 
			if unique_bitstrings == bitstring:
				counter += 1 

		#At this point we have the frequency of the iterative variable 

		new_value = []

		for i in range(counter):
			new_value.append(map_bitstring_digit(unique_bitstrings))


		my_dict.update({unique_bitstrings : new_value})


	return my_dict

# input_bitstring = ['10', '11', '01', '00', "10", '00', '00', '11', '10', '00', '00', '01', '01', '11', '10', '00', '11', '10', '11', '11']
# input_bitstring = ['00', '00', '11', '10']
# input_bitstring = []
# print(gather_by_values(input_bitstring))
	






