__author__ = 'szeitlin'

#"one small letter, surrounded by exactly three big bodyguards on each of its sides"

import re

newstring = ""

with open("bodyguards.txt") as myfile:
    for line in myfile:
        newstring += line.strip() #not sure if strip was actually required
        p = re.compile("(?<=[a-z])([A-Z]{3}[a-z][A-Z]{3}[a-z]+)") #lookbehind is (?<=...) where ... should be all caps
        q = p.findall(newstring)
    if len(q) >= 7:
        print q

#take only the small letter from each one:
answer = ""

for word in q:
    for char in word:
        if char.islower():
            answer += char
            break
print answer
