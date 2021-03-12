def write_chunks_of_five(words, fname): 
	"""
	The purpose of this function is to take a list of words and output them into a text file
	with 5 words per line 

	:param words(lst): Input string containing list of words
	:param fname(str): Name of output file

	"""

	assert isinstance(words, list)
	assert isinstance(fname, str)



	with open(fname,"w") as output: 
		
		for word in words:
			output.write(word)
			output.write(" ")
			if (((words.index(word)) + 1) % 5 == 0):
				output.write("\n")

