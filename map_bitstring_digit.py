def map_bitstring_digit(bitstring):
	"""
	The purpose of this function is to map one bitstring to a bit. If number of (0s > no of 1s) then the mapping is 0 else its.
	The output is a number 

	:param bitstring: Input bitstrings

	"""

	# assert isinstance(bitstring_list, list)

	# counter = True
	# for items in bitstring_list: 
	# 	assert(isinstance(items,str)) #Making sure each bitstring is a string
	# 	assert(items.isdigit() == True) #Making sure each bitstring only contains digits

	
	# for bits in bitstring_list:
	# 	for no in bits:
	# 		if (no != "1") and (no != "0"): #Making sure each bitstring only contains bits
	# 			print(no)
	# 			counter = False
	
	# assert (counter == True ) #Making sure each bitstring only contains bits

	#End of asserts



	
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



# x = ['100', '100', '110', '010', '111', '000', '110', '010', '011', '000']

print(map_bitstring_digit("1100"))



