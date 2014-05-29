__author__ = 'szeitlin'

#according to the hints, it sounds like they want you to write a regular expression and look for
#a three-letter string (consecutive characters that are all letters)
#not actually what they want, and not at all what I thought from the original description!

import re

newstring = ""

with open("ocr.txt") as myfile:
    for line in myfile:
        newstring += line.strip() #not sure if strip was actually required

    p = re.compile("[a-z]+") #[a-z] should give any letters a-z
    q = p.findall(newstring)
    if q != []:
        print q





