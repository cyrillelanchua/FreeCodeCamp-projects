
class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
      return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"

  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.height * self.width

  def get_perimeter(self):
    return 2*(self.width+self.height)
  def get_diagonal (self):
    return ((self.width ** 2 + self.height ** 2) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    string = ""
    paddingstar = "************************************************"
    for i in range(self.height):
        string += paddingstar[:self.width] + '\n'

    return string

  def get_amount_inside(self, shape):
    return self.get_area()//shape.get_area()
    
    
class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        super().__init__(side,side)
    def __str__(self):
        return "Square(side="+str(self.side)+")"
    
    def set_side(self,side):
        self.side = side
        super().set_height(side)
        super().set_width(side)
    def set_height(self, height):
        self.side = height
        super().set_height(height)
        super().set_width(height)
    def set_width(self, width):
        self.side = width
        super().set_height(width)
        super().set_width(width)

x = Rectangle(10,10)
x.set_height(8)
x.set_width(7)
print(x.get_picture())
p = Square(3)
p.set_side(4)
rer = str(x)
print(p)