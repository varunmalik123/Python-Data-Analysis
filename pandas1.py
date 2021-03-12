import pandas as pd 

def split_count(x): 
	"""
	Takes a csv as an input and returns a data frame with two columns with frequency of works in the a specific column in the csv

	:param x(csv): input csv
	"""
	import pandas as pd


	assert isinstance(x,pd.Series)

	
	from collections import defaultdict
	

	
	freq_dict = defaultdict(int)


	for index, value in my_data.items():
		split = value.split(",")
		
		for words in split:
			freq_dict[words] += 1



	df = pd.DataFrame(list(freq_dict.items()))



	df.set_index(0, inplace = True)

	df = df.sort_values(1)

	df = df.rename(columns = {0:'count'}) 

	return df


# x = pd.read_csv("survey_data.csv")
# my_data = x["Is there anything in particular you want to use Python for?"]


# split_count(my_data)
# df = pd.DataFrame(freq_dict)
# for i,o in freq_dict.items():
# 	print(i,o)


# for index, row in df.iterrows():
# 	print(index, row)

	


# def split_count(x):
# """ where x is a pd.Series object and it returns a pd.DataFrame object.
# """
