class Rectangle(object):
  def __init__(self, width, height):
    self.width = width
    self.height = height

  @property
  def area(self):
    return self.width * self.height

r = Rectangle(2, 3)
print r.area # look ma no parens!
