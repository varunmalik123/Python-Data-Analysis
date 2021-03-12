def compute_average_word_length(instring, unique = False): 
	avg_word_len = 0 
	word_array = []
	unique_array = []
	string = ""
	i = 0 

	for char in instring: 
		string += char
		i = i + 1 
		#print(char, i)

		
		if (char == " ") or (char == "\n") or (char == "\t") or (char == ".") or (i == (len(instring)) ): #A new word 
			stripped_str = string.strip() #Defining a new str becuase strings are immutable 
			
			if(char == "."):
				period_stripped_str =stripped_str.replace(".", "")
				word_array.append(period_stripped_str)
				string = ""
				continue #add it to a elif 

			print(len(stripped_str),stripped_str)
			word_array.append(stripped_str)
			string = ""
	
	print(word_array) 
	if (unique == False):
		avg_word_len = len(word_array)

	else: 
		[unique_array.append(words) for words in word_array if words not in unique_array]
		avg_word_len = len(unique_array)

	return avg_word_len

input = '''Varun is
	Varun Varun Varun. Varun.
	Varun. Varun. '''

print(compute_average_word_length(input))






