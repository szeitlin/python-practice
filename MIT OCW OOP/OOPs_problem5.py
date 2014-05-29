class Thing(object):  #recommended "new style classes" esp. for python 3
	def set (self, v):  #set is for validation
		self.x = v  	#self.x gets v as an argument to the method "set"
	def get (self):		#get is processing 
		return self.x
		
	def assignThing(self, thing1):
		#self_value = self.get()
		#thing1_value = thing1.get()
		self.set(thing1.get())
		#self.hasBeenAssigned = True
		
	def __str__(self):
		return str(self.get())
		
	def swapThing(self, thing1):
		print self, thing1
		temp1 = thing1.get()
		temp2 = self.get()
		new_self = self.set(temp1)
		new_thing = thing1.set(temp2)
		self.set = new_self
		thing1.set = new_thing
		print self, thing1
		
		#self.hasBeenSwapped = True
	
	def sumOfThings(self, thing1):            
		newThing = Thing()
		newThing.set(self.get() + thing1.get())
		print newThing
		
	def sumOfAllThings(self, temp_thing):
		"""method
		takes a list --> return a new Thing 
		where Thing.x = sum[list of things]"""
		some_things = Thing()  #creates a new Thing
		some_things.set(sum(temp_thing))  #takes the value of the sum of all the things
		print some_things	#returns the value of the new Thing (the sum)

bob = Thing()
bob.set(1)
print bob

terry = Thing()
terry.set(2)
print terry

# thing2.assignThing(thing1)
# print thing1.get()
# print thing2.get()

#print thing1.hasBeenAssigned

terry.swapThing(bob)

#print thing1.hasBeenSwapped 

bob.sumOfThings(terry)

thing_list = [1,2,3,4]
bob.sumOfAllThings(thing_list)

# some_things = Thing()
# some_things = []
# print some_things
# for Thing in thing_list:
# 	some_things.append(Thing)
# print some_things


# a = Thing()
# a.set(default)
# a.get()   
# a.x = 6 	#a is a Thing and it's okay to create a.x without having assigned it previously
# print a.get()   
#  
# b = Thing()
# a.set(b) 	#setting a.x to b
# print a.x 	#this just returns b
# 
# b.set(7) 
# print a.x.x   	# returns a.x is b and b.x is 7 
# 
# a.get()		#still b
# 
# a.x.get()	#same as a.x.x
# 
# 3 + a.get().get()  	#same as a.x.x + 3
# 
# c = a.get()     #same as b
# print c.x		#b.x is 7 
# 
# a.set(1 - a.get().get())  #a.x is -6
# print a.x
# 
# c.set(3)    #setting b.x to 3
# 
# a.get().get()  	#same as b.x which is 3
# 
# a = Thing()
# b = Thing()
# a.set(b)
# b.set(a)
# a.x == b    #bool
# 
# a.x.x == a   true
# a.x.x.x == b    true













