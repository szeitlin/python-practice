__author__ = 'szeitlin'



import urllib2
import zipfile

# info = urllib2.urlopen('http://pythonchallenge.com/pc/def/channel.html')
# print info

#if channel.zip already exists, skip this
target = 'http://pythonchallenge.com/pc/def/channel.zip'

response = urllib2.urlopen(target)

body = response.read()

with open("channel.zip", 'wb') as myfile:
    myfile.write(body)

#print zipfile.is_zipfile("channel.zip")

myfile = zipfile.ZipFile("channel.zip")

# print myfile.printdir()
#
# informy = myfile.infolist()
#
# commentlist = []
#
# for item in informy:
#     commentlist.append(item.comment)
#
# print ''.join(commentlist)



readme = myfile.read("readme.txt")

#print readme

first = myfile.read("90052.txt")

#print first

noted = first.split()
#print noted

second = myfile.read(noted[-1]+".txt")

#print second
#splitted = second.split()

#print splitted

lastfile = second

#print myfile.getinfo("90052.txt").comment

commentlist = []

def get_next_file(myfile, lastfile, commentlist):
    '''
      This worked correctly, then it said to collect the comments, which I had tried already.
      Trick was collecting them in the right order while iterating through the list of files, and exiting cleanly.

    Recursion to iterate through the files until you get to something that is not just a number.

    :param myfile: zip file
    :param lastfile: most recently read .txt file inside the zip file
    :return: (str) contents of .txt file that specifies the next file to read
    '''
    splitted = lastfile.split()
    #print splitted
    newname = splitted[-1]+".txt"
    nextfile = myfile.read(newname)
    #print nextfile
    commentlist.append(myfile.getinfo(newname).comment)
    #print nextfile
    return get_next_file(myfile, nextfile, commentlist)

try:
    get_next_file(myfile, lastfile, commentlist)
except KeyError:
    print ''.join(commentlist)




#note: bytes vs. unicode
#str in python 2 is a bytestring
#implicitly changes bytes into unicode
#binary or text mode for opening files, only matters on windows



#unicode is different in python 3
#str in python 3 is stored in codepoints (unicode string)
#if you want bytes in python3, do b"Hello World"
#what data you get depends on how you opened the file

#default text mode gives you unicode, binary mode gives you bytestring



#build a unicode sandwich
#bytes on the outside, unicode on the inside
#decode on the way in as fast as possible, encode on the way out as late as possible

