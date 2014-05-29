class Thing(object):  #recommended "new style classes" esp. for python 3
	def set (self, v):  #set is for validation
		self.x = v  	#self.x gets v as an argument to the method "set"
	def get (self):		#get is processing 
		return self.x

a = Thing()
a.set(default)
a.get()   
a.x = 6 	#a is a Thing and it's okay to create a.x without having assigned it previously
print a.get()   
 
b = Thing()
a.set(b) 	#setting a.x to b
print a.x 	#this just returns b

b.set(7) 
print a.x.x   	# returns a.x is b and b.x is 7 

a.get()		#still b

a.x.get()	#same as a.x.x

3 + a.get().get()  	#same as a.x.x + 3

c = a.get()     #same as b
print c.x		#b.x is 7 

a.set(1 - a.get().get())  #a.x is -6
print a.x

c.set(3)    #setting b.x to 3

a.get().get()  	#same as b.x which is 3

a = Thing()
b = Thing()
a.set(b)
b.set(a)
a.x == b    #bool

a.x.x == a   true
a.x.x.x == b    true













