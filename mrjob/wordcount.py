import sys
from collections import defaultdict

words=defaultdict(int)

for line in sys.stdin:
	for line in line.split():
		words[word] += 1

for word, count in sorted(words.items()):
	print'%s was found %d times' % (word, count)

#problem is that this is all in memory (storing)


