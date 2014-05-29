## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

   def __init__(self):
    pass

   def eat(self, food):
	self.food = food
	print "I ate the " + food

## Dog is an animal
class Dog(Animal):

    def __init__(self, name):
        # the dog has a name
        self.name = name
	print "the dog's name is " + name

## Cat is an animal
class Cat(Animal):

    def __init__(self, name):
        # the cat has a name
        self.name = name

    def __str__(self):
	pet.name = name
	print " the cat's name is " + name

## Person is an object
class Person(object):

    def __init__(self, name):
        ## the person has a name
        self.name = name
	print "the owner's name is " + name
	
        ## Person has-a pet of some kind
        self.pet = None

    def get_pet(self):
	return self.pet
	
## Employee is a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic? I have no idea. 
        super(Employee, self).__init__(name)
        ## Employee has a salary
        self.salary = salary

## Fish is an object
class Fish(object):
    pass

## a Salmon is a Fish
class Salmon(Fish):
    pass

## A Halibut is a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat named Satan
satan = Cat("Satan")

## Mary is a Person named Mary
mary = Person("Mary")

## Mary's cat is Satan
mary.pet = satan
c = mary.get_pet()
print c

print "mary's pet's name is " + pet_name

##try to make mary's cat eat something
satan.eat("mice")
print "mary's cat " + mary.pet + " ate the " + food

## Frank is an Employee who makes 120,000
frank = Employee("Frank", 120000)

## Frank's pet is rover
frank.pet = rover

## Flipper is a Fish
flipper = Fish()

## Crouse is a Salmon
crouse = Salmon()

## Harry is a Halibut?
harry = Halibut()
