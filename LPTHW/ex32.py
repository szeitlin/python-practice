the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print "this is count %d" %number

#same
for fruit in fruits:
	print "A fruit of type: %s" % fruit

#and mixed lists have to use %r if you don't know what's in it
for i in change:
	print "I got %r" % i

#to build a list, start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
#for i in range (0, 6):

i = 1

if i < "5":
	i = i + 1
	print "Adding %d to the list." %i
	#append is a function for the list to use
	elements.append(i)


#and then print the list out
for i in elements:
	print "Element was: %d" % i
	