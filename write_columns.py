def write_columns(data,fname):
	"""
	The purpose of this function is to take a list of numbers and perform two calculations on it.
	The function will generate a csv file with three columns containing the original data and the 
	result from the first to calculations respectively 

	:param data(list with elements being either floats or ints): Input data 
	:param fname(str): File name of output csv 
	"""
	assert isinstance(data, list)
	assert isinstance(fname, str)
	assert (len(data) > 0)
	for elements in data: 
		assert isinstance(elements, (int, float))

	import csv 
		
	fname = fname + ".csv"

	with open(fname, "w") as out: 
		
		big_big = []
		for no in data: 
			temp_list = []
			temp_list.append('{0:.2f}'.format(no))
			temp_list.append(" " + '{0:.2f}'.format((no**2)))
			temp_list.append(" " + '{0:.2f}'.format(((no + no**2)/3)))
			big_big.append(temp_list)

		writer = csv.writer(out)
		writer.writerows(big_big)
