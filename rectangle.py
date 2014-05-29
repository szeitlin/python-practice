class Rectangle(object):
  def __init__(self, width, height):
    self.width = width    
    self.height = height
    self.area = width * height

r = Rectangle(2, 3)
print r.area
