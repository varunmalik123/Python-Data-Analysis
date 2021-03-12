def get_sample(nbits=3,prob=None,n=1):
	"""
	This function takes the dictonary prob as an input and returns n number of random bits of
	size nbits from the dictionary depending on their probability mass 

	:param nbits(int): The size of input and output bits
	:param prob(dict): Input dictionary with Keys being each FLOAT bits of size n and values being pmf
					   of each bit. pmf are floats with sum(total) == 1
	:param n(int): Number of bits to return
	"""

	import itertools
	import random

	assert isinstance(nbits, int)
	assert isinstance(prob, dict)
	assert isinstance(n,int)

	assert nbits > 0 
	assert n > 0 


	for keys,values in prob.items():  
		assert(isinstance(keys,str)) #Asserting keys are strings of bits
		assert (isinstance(values,float) or isinstance(values,int)) #Asseting Values are floats


	total_prob = 0
	for probability in prob.values(): #Asserting that total prob doesnt exceed 1 
		total_prob += probability
		assert probability >= 0 #Asseting each single prob values arent negative

	for bits in prob.keys(): 
		assert len(bits) == nbits 
		assert (bits.isdigit() == True)

	counter = True
	for bits in prob.keys():  #Asserting input keys are bits only
		for no in bits: 
			if (no != "1") and (no != "0"):
				counter = False
	assert (counter == True )


	assert total_prob <= 1.0



	all_bits_tuples = itertools.product([1,0], repeat = nbits) #Generating all possible list combinations

	all_bits_list = [] #List that contains all bits combinations

	for items in all_bits_tuples: #Putting all possible bit combinations into a list
		temp = ""
		for no in items: 
			temp += str(no)
		all_bits_list.append(temp)

	prob_keys_list = [] #list that contains all values of the input dict
	prob_values_list = []

	for keys in prob.keys(): #adding keys to list
		prob_keys_list.append(keys)

	for values in prob.values(): #adding values to a list
		prob_values_list.append(values)

	all_bits_counter =  all(elem in prob_keys_list for elem in all_bits_list) #checking if prob_keys_list contains all values from all_bits_list

	assert all_bits_counter == True 

	#assertions end


	sample_list = random.choices(prob_keys_list, weights = prob_values_list, k = n)

	return sample_list








