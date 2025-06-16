# Task 4: Polymorphism with Collections – Shape Drawing

class Shape:
  def draw(self):
    pass

class Circle(Shape):
  def draw(self):
    print("Drawing a Circle")

class Rectangle(Shape):
  def draw(self):
    print("Drawing a Rectangle")

class Triangle(Shape):
  def draw(self):
    print("Drawing a Triangle")

circle = Circle()
circle.draw()
rectangle = Rectangle()
rectangle.draw()
triangle = Triangle()
triangle.draw()