__author__ = 'szeitlin'

# examples from James Powell.

def function(x):
    return x+1, x+2

assert function(10) == (11,12)

answer=function(10)

print 'function(10) -> {}'.format(answer)


def generator(x):
    yield x+1
    yield x+2

assert list(generator(10))==[11,12]

for x in generator(10):
    print 'generator(10) ->{}'.format(x)

#this is instead of reading the whole thing into memory and using indexing


###
gnratr_expression = ((x+1) for x in [1,2,4,8,16]) #have to change the name to re-instantiate

#assert list(generator_expression) == [2,3,5,9,17] #generators don't store the values they generate, can only be run once

for x in gnratr_expression:
    print 'generator_expression ->{}'.format(x)




###
gen_express =  lambda: ((x+1) for x in [1,2,4,8,16]) #using lambda makes it more like a function

assert(list(gen_express())) == [2,3,5,9,17]

for x in gen_express():
    print 'generator_expression() -> {}'.format(x)

