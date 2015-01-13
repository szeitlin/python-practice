__author__ = 'szeitlin'

#hint says to unpickle the banner.p file

import pickle
import urllib2

response = urllib2.urlopen('http://pythonchallenge.com/pc/def/banner.p')

obj = pickle.load(response)

#looks like list of list of tuples that might form a picture

#had to use a hint

for ele in obj:
    print "".join([e[0]*e[1] for e in ele])



#I didn't know you can put a list comprehension inside join??
#also how the fuck were you supposed to know that this is what you were supposed to do?