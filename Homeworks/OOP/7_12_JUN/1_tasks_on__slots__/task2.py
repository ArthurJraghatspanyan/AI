# Task 2: Attribute Restriction

class Car:
  __slots__ = ['brand', 'year']

  def __init__(self, brand, year):
    self.brand = brand
    self.year = year

car = Car("Audi", "2006")

car.color = "Black"         # AttributeError