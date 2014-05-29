__author__ = 'szeitlin'

# examples from James Powell.

#__call__ corresponds to () or apply()

class Callable(object):

    def __call__(self, x):
        return x+1, x+2

assert Callable()(10)==(11,12)

answer = Callable()(10)
print 'Callable(10 ->{}'.format(answer)


class Callable20(object):
    @staticmethod
    def __call__(x):
        return x+1, x+2

assert Callable20()(10)==11,12

#Iterables are the Python generalisation of lists, tuples, &c.
# In Python an iterable is just some object that supports the __iter__ protocol and returns an object which
# supports the __next__ protocol. __iter__ corresponds to iter() and __next__ corresponds to next()
# Note that in Python 2, the __next__ protocol is provided by next. This was fixed in Python 3

