def get_min_split(seq):
	"""
	Given an array of unique positive integers, divide the array into two subsets 
	such that the absolute difference between the respective sums of the subsets 
	is as small as possible.
	
	:param seq(list): Input sequence

	"""
	import numpy as np 

	# assert isinstance(seq,(list,np.ndarray))
	# assert len(seq) > 0 
	assert isinstance(seq, np.ndarray) or isinstance(seq, list)
	# for elem in list(seq):
	# 	assert (isinstance(elem,int) or np.issubdtype(type(elem), np.integer))

	import itertools
	from collections import defaultdict

	if type(seq) == np.ndarray:
		seq = np.array(seq).tolist()

	list_l = seq[:]

	out = []
	out_full = []
	my_dict = defaultdict(list)

	for i in range(1, len(list_l)):
		out = list(itertools.combinations(list_l, i))
		out_full.append(out)

	out_full = out_full[len(out_full)//2:]
	new = []
	for items in out_full:
		for tuples in items: 
			new.append(list(tuples))

	# print(new)

	for sublists in new: 
		
		given_list = seq[:]
		
		for item in sublists:
			given_list.remove(item)


		key = abs(sum(given_list) - sum(sublists))
		
		# old_value = my_dict[key]

		value = []

		# print(value)
		value.append(sublists)
		value.append(given_list)
		
		# new_value = old_value  

		# print(value)
		# print("\n")
		my_dict[key].append(value)


	for key,value in my_dict.items():
		for pairs in value:
			tuple(pairs) 

	dict_t = defaultdict(list)

	for key,value in my_dict.items():
		for pairs in value: 
			new_value_t = tuple(pairs)
			dict_t[key].append(new_value_t)
		
	# for i,o in dict_t.items():
	# 	print(i,o)

	# print("\n\n\n")
	smallest_sum = (min(dict_t))

	return dict_t[smallest_sum]

# seq = np.array([1, 6, 11, 5])
# print(get_min_split(seq))

