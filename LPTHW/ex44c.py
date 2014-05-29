class Parent(object):

	def __init__(self):
		pass

	def override(self):
		print "PARENT override()"

	def implicit(self):
		print "PARENT implicit()"

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def override(self):
		print "CHILD override()"                #this overrides the parent version of override

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self). altered() 		#calls the parent version of altered() and runs that on Child 
		print "CHILD, AFTER PARENT altered()"

#is calling the super version technically overriding the local version? or is that not called an override?

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


###

class Child2(Parent):

	def __init__(self, stuff):
		self.stuff = stuff
		super(Child2, self). __init__()
		print "initialized CHILD2 with stuff = " + stuff

bob = Child2("foo")
