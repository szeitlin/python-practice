def foo():
  b = BankAccount()
  b.deposit(10)
  return b

b = foo()

print b.deposited

#In this case, the object we passed to deposit() was a temporary literal, and we can access its value outside of foo(), because the object is remembering the value. 
