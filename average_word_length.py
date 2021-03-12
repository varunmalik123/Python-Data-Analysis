def compute_average_word_length(instring, unique = False): 
	
	"""
	The purpose of this program is to compute the average word length given an input string. 
	If the unique input is set to True, the program disregards repeated words and computes the 
	average word length 

	:param instring(string): Input String 
	:param unique(Bool): Toggle uniqueness On/Off

	"""
	assert isinstance(instring, str)
	assert isinstance(unique, bool)
	assert (len(instring) > 0)
	
	average = 0
	word_array = instring.split()
	no_chars = 0 

	if (unique == True):
		unique = []
		for words in word_array:
			if words not in unique:
				unique.append(words)

		length = (len(unique))
		
		for words in unique:
			no_chars += len(words)

		average = no_chars/length

	else: 
		length = (len(word_array))

		for words in word_array:
			no_chars += len(words)
		average = no_chars/length

	return average


#can also use set 
#string.punctuation 




