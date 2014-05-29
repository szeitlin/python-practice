#!/usr/local/bin/python

import sys

for line in sys.stdin:
	words=line.split()
	for word in words:
		print "%s\t%d" % (word,1)


