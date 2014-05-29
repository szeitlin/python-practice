class Thing(object):  #recommended "new style classes" esp. for python 3
	def set (self, v):  #set is for validation
		self.x = v  	#self.x gets v as an argument to the method "set"
	def get (self):		#get is processing 
		return self.x
	
	def mangle(self):
		self.set(self.get() + 1)
		self.hasBeenMangled = True
		
a = Thing()
a.set(3)
print a.get()

a.mangle()
print a.get()
		
		