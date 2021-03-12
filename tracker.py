from time import sleep
import random
from datetime import datetime
import itertools as it

import types 

def producer():
	'produce timestamps'
	starttime = datetime.now()
	while True:
		sleep(random.uniform(0,0.2))
		yield datetime.now()-starttime

p = producer()


def tracker(p,limit):

	"""
	The purpose of this function is to run the generator p and count the odd number values in p until limit is reached. 
	We can also chnage the value of limit midway

	:param p(generator): Input generator function that is to be run
	:param limit(int): Limit how many odd interations the generator will go till 
	"""


	assert isinstance(p, types.GeneratorType)
	assert isinstance(limit, int)
	assert (limit >= 0)

	counter = 0

	while limit > 0:
		a = next(p).seconds

		if (a % 2 == 0): #Even
			b = yield counter

		else:
			counter += 1
			#print(a)
			limit -= 1
			b = yield counter

		if isinstance(b,int):
			assert (b >= limit)
			limit = b - counter


# t = tracker(p,limit=6)
# next(t)
# next(t)

# t.send(6)
# print(list(t))

