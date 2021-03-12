

	def __add__(self,other):
		assert isinstance(other, Interval)
		
		if self._iscontained(other):
			return Interval(other._a, other._b)
		
		elif self._iscontained(other):
			return Interval(self._a + other._a, self._b + other._b)
		else:
			raise NotImplementedError
	def _iscontained(self, other):
			if self._a < other._a and other._b < self._b:
				return False
			else:
				return True
	def __repr__(self):
			return '|%d,%d|'%(self._a, self._b)
         
          


a = Interval(3,8)
b = Interval(4,5)

print(a+b)
#           def __eq__(self,other):
#              pass
#           def __lt__(self,other):
#              pass
#           def __gt__(self,other):
#              pass
#           def __ge__(self,other):
#              pass
#           def __le__(self,other):
#              pass
# ----interval----

# implement __eq___ function 

# implement __repr___

# testing a+b == b+a 

# can only intervals , check other(b) is also an interval object

# As