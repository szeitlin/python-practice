class Thing(object):  #recommended "new style classes" esp. for python 3
        def set (self, v):  #set is for validation
                self.x = v      #self.x gets v as an argument to the method "set"
        def get (self):         #get is processing 
                return self.x
        
        def mangle(self):
                self.set(self.get() + 1)
                self.hasBeenMangled = True
                
        def clone(self):
                newThing = Thing()
#               newThing.set(self.get())
                value = self.get()
                newThing.set(value)
                return newThing
                
        def __str__(self):
                return "This is a Thing with value " + str(self.get())
                
                
a = Thing()
a.set(3)
print a
b = a.clone()
b.get()

a.mangle()
print a.get()
print b
