__author__ = 'szeitlin'


# urllib may help. DON'T TRY ALL NOTHINGS, since it will never
# end. 400 times is more than enough. -->
# <center>
# <a href="linkedlist.php?nothing=12345"><img src="chainsaw.jpg"

import urllib2

#doesn't matter where you enter the list, you get the same numbers back.

i = 87130

longlist = []

for i in range(1000):
    response = urllib2.urlopen('http://pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(i))
    j = response.read()
    print j
    j = j.rsplit()
    i = j[-1]
    longlist.append(i)

print longlist

#this doesn't work; seems like I need an opener and a handler for php? or a post request?

