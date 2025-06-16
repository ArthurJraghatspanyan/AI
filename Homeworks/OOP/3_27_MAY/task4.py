# # TASK 4: Norm Method Using Polymorphism (Vector and Matrix)

class BaseNorm:
  
  def norm(self):
    pass

class Vector:
  def __init__(self, data: list):
    self.data = data
  
  def norm(self):
    if not isinstance(self.data, list):
      raise TypeError("Type must be List.")
    if not self.data:
      raise ValueError("List must not be empty.")
    res = 0
    for i in self.data:
      if not isinstance(i, int):
        raise TypeError("Elements must be integer type.")
      res += i ** 2

    return f"{res ** 0.5:.5f}"

class Matrix:
  def __init__(self, data: list):
    self.data = data
  
  def norm(self):
    if not isinstance(self.data, list):
      raise TypeError("Type must be List.")
    if not self.data:
      raise ValueError("List must not be empty.")
    sum_of_squared = 0
    for i in self.data:
      if not isinstance(i, list):
        raise TypeError("Type must be List.")
      for j in i:
        sum_of_squared += j ** 2
    res = sum_of_squared ** 0.5
    return f"{res:.5f}"

ls = [Vector([1, 2, 3, 4]), Matrix([[10, 20], [30, 40]])]

for i in ls:
  print(i.norm())