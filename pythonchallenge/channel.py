__author__ = 'szeitlin'


#import base64
import codecs
import string
#import unicodedata
import urllib2
import zipfile

# info = urllib2.urlopen('http://pythonchallenge.com/pc/def/channel.html')
# print info


response = urllib2.urlopen('http://pythonchallenge.com/pc/def/channel.zip')


with open("channel.txt", 'wb') as myfile:
    for tup in response:
        decoded = [codecs.decode(x, 'ascii', 'ignore') for x in tup]
        #decoded = [codecs.decode(x, 'latin-1', 'replace') for x in tup]
        chunk = ''.join(decoded) #this returns something human-readable, but in need of further parsing to get rid of ASCII control characters
        readable = filter(string.printable.__contains__, chunk)
        #print readable
        myfile.write(readable)
        splitted = readable.split() #if you don't do the string.prinatable step, this returns list of code points again???

        #once that's parsed into filenames without extra/null unicode characters, can do this:
        for filename in splitted:
            print '%5s %s' %(filename, zipfile.is_zipfile(filename))


#really what I want to do is look at the readme file inside the zip archive, don't know how to do that 



# unzipped = zip(*response)
# print unzipped.read(100)
#can I open this as utf-8 to begin with-?
#can I tell what the encoding is?


# for tup in unzipped:
#      decoded = [codecs.decode(x, 'latin_1', 'replace') for x in tup] #, errors='ignore')
     #print decoded
     #print ''.join(decoded)


     # for i, c in enumerate(decoded):
     #    print i, '%04x' % ord(c), unicodedata.category(c),
     #    try:
     #        print unicodedata.name(c)
     #    except ValueError:
     #        continue



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

