def thingMangle(arg):      #just a function but it depends on the previous class Thing
	arg.set(arg.get() + 1)
	arg.hasBeenMangled = True

a = Thing()
a.set(5)
thingMangle(a)
print a.get()

print a.hasBeenMangled

b = Thing()
b.set(Thing())
b.get().set(3)
thingMangle(b.get()) 
print b.get()  	#just tells you that b.x is a Thing (from line 13)
print b.get().get()    #returns 4

c = Thing()
thingMangle(c) 	#error


