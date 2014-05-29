


def listy():
	
	print "give me a number and I'll list all the numbers up to it"

	n = input("> ")

	i = 0
	numbers = []
	
	while i < n:
		print "At the top i is %d" % i
		numbers.append (i)
	
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

		print "the numbers: "

		for num in numbers:
			print num
	else:
		exit()	
	

listy()

#this sort of worked - there is a difference between raw_input() and input()
#when I do it with raw_input() it doesn't stop at n - raw_input() treats it as a string, 
#but input() treats it as a python expression

