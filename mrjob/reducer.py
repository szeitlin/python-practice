#!/usr/local/bin/python

import sys

def output(previous_key, total):
	if previous_key is not None:
		print "%s was found %d times" % (previous_key, total)

previous_key = None
total =0

for line in sys.stdin:
	key, value=line.split("\t",1)
	if key != previous_key:
		output(previous_key, total)
		previous_key=key
		total=0
	total += int(value)

output(previous_key, total)

#this is written assuming things are coming in sorted order, which is hadoop magic - 
#it sorts the keys before passing them
#to the reducer

#www.pinaldave.com/bimg/mapreduce.jpg --> diagram showing how mapreduce works
#blog.sqlauthority.com

