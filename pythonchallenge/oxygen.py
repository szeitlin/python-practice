__author__ = 'szeitlin'

# use selenium virtualenv for this, that's where Pillow 2.5.1 currently lives
# note that to use it, you have to know it's called PIL for python imaging library

from PIL import Image
from PIL import PngImagePlugin as png
import urllib2

target = 'http://pythonchallenge.com/pc/def/oxygen.png'

response = urllib2.urlopen(target)

body = response.read()

#print body

with open("oxygen.png", 'wb') as myfile:
    myfile.write(body)

im = Image.open("oxygen.png")
#im.show()

chunky = png.PngStream(im)

chunks_are_us = png.getchunks(im)

for item in chunks_are_us:
    print item[0]

#this returns these:
# IHDR (required)
# IDAT (image data chunk 1)
# IDAT (image data chunk 2)
# IEND (required)

#this works but is not informative
# for k,v in im.info.iteritems():
#     print k,v


