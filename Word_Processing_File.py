def get_average_word_length(words):
	"""
	This function returns the average length of words given a list of words 

	:param words(list): Each entry is a string of a word
	"""

	assert isinstance(words, list) #asserting that input is a list
	assert len(words) > 0 #list isn't empty
	for items in words:
		assert isinstance(items, str) #Each item is a word
		assert len(items) > 0 #Items aren't empty

	stripped_words = []
	
	for strings in words: 
		stripped_words.append(strings.strip()) #take out white space


	total_length = 0

	for word in stripped_words:
		for letters in word: 
			total_length += 1


	total_words = len(stripped_words)


	average_word_len = total_length / total_words

	return (total_words, total_length, average_word_len)



def get_longest_word(words):
	"""
	This function returns longest word given a list of words 

	:param words(list): Each entry is a string of a word
	"""

	assert isinstance(words, list) #asserting that input is a list
	assert len(words) > 0 #list isn't empty
	for items in words:
		assert isinstance(items, str) #Each item is a word
		assert len(items) > 0 #Items aren't empty

	stripped_words = []
	
	for strings in words: 
		stripped_words.append(strings.strip()) #take out white space

	longest_word = ""

	for word in stripped_words:
		if len(word) > len(longest_word):
			longest_word = word 

	return longest_word


def get_longest_words_startswith(words,start):
	"""
	This function returns longest word that starts with the letter start, given a list of words 

	:param words(list): Each entry is a string of a word
	:param start(str): The specific word start length
	"""

	assert isinstance(words, list) #asserting that input is a list
	assert isinstance(start, str)
	assert len(start) == 1
	assert len(words) > 0 #list isn't empty
	for items in words:
		assert isinstance(items, str) #Each item is a word
		assert len(items) > 0 #Items aren't empty

	stripped_words = []
	
	for strings in words: 
		stripped_words.append(strings.strip()) #take out white space


	longest_word = ""

	for word in stripped_words:
		if word[0] == start:
			if len(word) > len(longest_word):
				longest_word = word
	
	return longest_word


def get_most_common_start(words):
	"""
	This function returns the most common starting letter from a list of words 

	:param words(list): Each entry is a string of a word
	"""

	assert isinstance(words, list) #asserting that input is a list
	assert len(words) > 0 #list isn't empty
	
	for items in words:
		assert isinstance(items, str) #Each item is a word
		assert len(items) > 0 #Items aren't empty

	stripped_words = []
	
	for strings in words: 
		stripped_words.append(strings.strip()) #take out white space

	start_words_list = []


	for word in stripped_words:
		start_words_list.append(word[0])

	start_words_list_set = set(start_words_list)

	return max(start_words_list_set, key = start_words_list.count)


def get_most_common_end(words):
	"""
	This function returns the most common ending letter from a list of words 

	:param words(list): Each entry is a string of a word
	"""

	assert isinstance(words, list) #asserting that input is a list
	assert len(words) > 0 #list isn't empty
	
	for items in words:
		assert isinstance(items, str) #Each item is a word
		assert len(items) > 0 #Items aren't empty

	stripped_words = []
	
	for strings in words: 
		stripped_words.append(strings.strip()) #take out white space

	end_words_list = []

	for word in stripped_words:
		end_words_list.append(word[-1])

	end_words_list_set = set(end_words_list)

	return max(end_words_list_set, key = end_words_list.count)



# ##### Testing ####
# from urllib.request import urlopen
# u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
# response = urlopen(u)
# words = [i.strip().decode('utf8') for i in response.readlines()]

# words_list = words[:20]

# a = get_most_common_end(words_list)
# print(words_list)
# print(a)


