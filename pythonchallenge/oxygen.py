__author__ = 'szeitlin'

# use selenium virtualenv for this, that's where Pillow 2.5.1 currently lives
# note that to use it, you have to know it's called PIL for python imaging library

from PIL import Image
from PIL import PngImagePlugin as png
from PIL import ImageFile
import urllib2

target = 'http://pythonchallenge.com/pc/def/oxygen.png'

response = urllib2.urlopen(target)

body = response.read()

#print body

with open("oxygen.png", 'wb') as myfile:
    myfile.write(body)

fp = open("oxygen.png", 'r')

p = ImageFile.Parser()

while True:
    s = fp.read(629)
    print s
    if not s:
        break
    p.feed(s)

im = p.close()

im.save("o2.png")

#im.show()

# chunky = png.PngStream(im)

chunks_are_us = png.getchunks(fp)



#for item in chunks_are_us:
    #print item[0]
#this returns these:
# IHDR (required)
# IDAT (image data chunk 1)
# IDAT (image data chunk 2)
# IEND (required)

#no itXt chunk or other metadata
#this works but is not informative
# for k,v in im.info.iteritems():
#     print k,v

#assume the relevant information is in the image data itself

idat1 = chunks_are_us[1]
idat2 = chunks_are_us[2]

print idat2

#ideas: could be pattern of rows and columns, or grey level codes-?

#could try translating the bytes to see if any of them are text (doesn't look like they are?)



