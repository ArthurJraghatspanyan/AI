# Abstract Class – Shape Area Calculator

from abc import ABC, abstractmethod


class Shape(ABC):
  @abstractmethod
  def area(self) -> float:
    """Return the area of the shape"""
    pass

  @abstractmethod
  def name(self) -> str:
    """Return the name of the shape"""
    pass


class Circle(Shape):
  def __init__(self, radius: int):
    self.radius = radius

  def area(self):
    if not isinstance(self.radius, int):
      raise TypeError("Type of radius must be integer...")
    if self.radius <= 0:
      raise ValueError("Radius must be greater than 0...")
    return 3.14 * self.radius ** 2

  def name(self):
    return self.__class__.__name__


class Rectangle(Shape):
  def __init__(self, width: int, height: int):
    self.width = width
    self.height = height

  def area(self):
    if not isinstance(self.width, int) or not isinstance(self.height, int):
      raise TypeError("Type of width and/or height must be integer...")
    if self.width <= 0 or self.height <= 0:
      raise ValueError("Value of width and/or height must be greater than 0...")
    return self.width * self.height
  
  def name(self):
    return self.__class__.__name__


class Triangle(Shape):
  def __init__(self, base: int, height: int):
    self.base = base
    self.height = height
  
  def area(self):
    if not isinstance(self.base, int) or not isinstance(self.height, int):
      raise TypeError("Type of base and/or height must be integer...")
    if self.base <= 0 or self.height <= 0:
      raise ValueError("Value of width and/or height must be greater than 0...")
    return (self.base * self.height) / 2

  def name(self):
    return self.__class__.__name__

def print_area(shape: Shape):
  print(f"{shape.name()} area: {shape.area():.2f}")

def main():
  shapes = [Circle(3), Rectangle(4,5), Triangle(6, 2)]

  for shape in shapes:
    print_area(shape)

if __name__ == '__main__':
  main()