class Foo(object):
  def __init__(self, title):
    self.title = title
  def copy_from(self, other_obj):
    self.title = other_obj.title

a = Foo("Ha!")
b = Foo("Ha ha!")

a.copy_from(b)
print a.title
