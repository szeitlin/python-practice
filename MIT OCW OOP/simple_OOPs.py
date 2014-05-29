class Car:
	color = 'gray' 	#color is a member of the class
	
	def describeCar(self):
		return 'A cool ' + Car.color + ' car' 
	def describeSelf(self):
		return 'A cool ' + self.color + ' car'
		
nona = Car()
print nona.describeCar()
print nona.describeSelf()

print nona.color 	#typed directly in the interpreter, it will print

lola = Car()
lola.color = 'plaid'
print lola.describeCar() #gray

print lola.describeSelf() #plaid

print lola.color

print nona.describeSelf()

nona.size = 'small'
print lola.size   

Car.size = 'big'
print lola.size

print nona.size 

