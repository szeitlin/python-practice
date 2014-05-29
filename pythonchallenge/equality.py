__author__ = 'szeitlin'

#"one small letter, surrounded by exactly three big bodyguards on each of its sides"

#I wonder if that includes above and below as well as right and left?

#let's try right and left first

import re

newstring = ""

with open("bodyguards.txt") as myfile:
    for line in myfile:
        newstring += line.strip() #not sure if strip was actually required
        p = re.compile("(?<=[a-z])([A-Z]{3}[a-z][A-Z]{3}[a-z]+)") #[a-z] should give any letters a-z
        q = p.findall(newstring)
    if len(q) >= 7:
        print q

#want the look before and look after assertions

#lookbehind is (?<=...) where ... should be all caps

#take only the small letter from each one:
answer = ""

for word in q:
    for char in word:
        if char.islower():
            answer += char
            break
print answer
