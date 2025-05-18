class Circle:
  def __init__(self, radius: float):
    if not isinstance(radius, (int, float)):
      raise TypeError("Type of radius must be integer or float!")
    if radius < 0:
      raise ValueError("Radius must be grater than or equal 0!")
    self.radius = radius

  def area(self):
    result = 3.14 * self.radius ** 2
    return result

  def perimeter(self):
    result = 2 * 3.14 * self.radius
    return result

  def display(self):
    return self.__str__()

  def __str__(self):
    return f"\nRadius: {self.radius},\nArea: {self.area()},\nPerimeter: {self.perimeter()}\n"

class Rectangle:
  def __init__(self, length: float, width: float):
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
      raise TypeError("Types of length and/or width must be integer or float!")
    if length <= 0 or width <= 0:
      raise ValueError("Length and/or width must be greater than 0!")

    self.length = length
    self.width = width

  def area(self):
    result = self.length * self.width
    return result

  def perimeter(self):
    result = 2 * (self.length + self.width)
    return result

  def display(self):
    return self.__str__()

  def __str__(self):
    return f"\nLength: {self.length},\nWidth: {self.width},\nArea: {self.area()},\nPerimeter: {self.perimeter()}\n"

class Triangle:
  def __init__(self, side1: float, side2: float, side3: float):
    if not isinstance(side1, (int, float)) or not isinstance(side2, (int, float)) or not isinstance(side3, (int, float)):
      raise TypeError("Types of sides must be integer of float!")
    if side1 + side2 < side3 or side2 + side3 < side1 or side1 + side3 < side2:
      raise ValueError("Sum of first two sides must be greater than third side!")

    self.side1 = side1
    self.side2 = side2
    self.side3 = side3

  def perimeter(self):
    result = self.side1 + self.side2 + self.side3
    return result

  def area(self):
    s = self.perimeter() / 2
    result = (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    return result

  def display(self):
    return self.__str__()

  def __str__(self):
    return f"\nSide1: {self.side1},\nSide2: {self.side2},\nSide3: {self.side3},\nArea: {self.area()},\nPerimeter: {self.perimeter()}\n"

def final_shape(shape_choosing: str, shapes: list):
  if not shape_choosing.lower() in shapes:
    raise ValueError("Enter right shape")
  elif shape_choosing.lower() == shapes[0]:
    radius = float(input("Enter radius: "))
    shape = Circle(radius=radius)
  elif shape_choosing.lower() == shapes[1]:
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    shape = Rectangle(length=length, width=width)
  elif shape_choosing.lower() == shapes[2]:
    side1 = float(input("Enter side1: "))
    side2 = float(input("Enter side2: "))
    side3 = float(input("Enter side3: "))
    shape = Triangle(side1=side1, side2=side2, side3=side3)
  return shape

shapes = ["circle", "rectangle", "triangle"]

while True:
  shape_choosing = input("Enter 'Stop' to stop the program.\n\nChoose a shape from these -> Circle, Rectangle, Triangle: ")
  if shape_choosing.lower() == 'stop':
    break

  final_shape_obj = final_shape(shape_choosing, shapes)
  print(final_shape_obj.display())