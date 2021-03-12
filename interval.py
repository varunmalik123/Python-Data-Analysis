class Interval(object):
    def __init__(self, a, b):
        """
        The purpose of this class is to add two Interval objects that represent
        a one-dimensional open interval on the real line

        :param a(int): integer
        :param b(int): integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        return '|%d,%d|'%(self._a, self._b)

    def __eq__(self, other):
        assert isinstance(other, Interval)
        return self._a==other._a and self._b==other._b

    def __add__(self, other):
        assert isinstance(other, Interval)
    
        if (self._a>other._a and self._a<other._b) or (self._b>other._a and self._b<other._b): #Checking for overlap case
            return Interval(min(self._a,other._a),max(self._b,other._b))
        

        elif (other._a>self._a and other._a<self._b) or (other._b>self._a and other._b<self._b):
            return Interval(min(self._a, other._a), max(self._b, other._b))
        

        else: #No overlap. Special case. Return both objects in a list
            return [self,other]

# a = Interval(1,3)
# b = Interval(2,4)
# c = Interval(5,10)

# x = b + c

# print((x))




