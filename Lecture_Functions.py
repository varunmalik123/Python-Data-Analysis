"""
The documentation of a function should be longer that the entire function itself 

USE ASSERTS 
 1) Can use assert to check input type 
 2) To check logic, e.g. Assert sum(probability) == 1 # This builds in a logic check into the function


pPrints are only for human consumption 


def function(*args):

	#This means means that this function is expecting to take an unknown number of number argumensta nd it stores it into a tuple clalled args


def function(a,b, *args):

>> function(1,2,3,4,5)
 ---> a = 1 
 b = 2 

 args = (3,4,5)

function(*t):

if t is (1,2,3,4,5)

and it this the same function that takes in arguments (a,b,*args). doing *t puts 1 in a, 2 in b and (3,4,5) in *args. 
*t is a way of unpacking a tuple into the args 


**kwargs() / **kwds --> puts captures argments that have key = value into a dict
*args  --> captures single arguments (values) in a tuple. 


If i try to run a function in a def of anotehr function, THE FUNCTION BODY will not run until teh function is called. This is becasue python "lazy evaluates" functions! 

However, if I call another function in the func signature of another func, it will be evaluated 
"""