def is_string_integer(char): 
	"""
	Checks if char is a base 10 integer and returns a Boolean value. 

	:param char: Input string. Can only contain one character
	:type char: str

	"""

	boolean = char.isdigit()

	assert isinstance(char,str)
	assert len(char) == 1

	return boolean



