# TASK 5: Pretty Print Matrix and Vector with __repr__ Overloading

class Vector:
  def __init__(self, *args):
    self.data = args
    self.ls = []
    for i in self.data:
      if not isinstance(i, int):
        raise TypeError("Type must be integer...")
      self.ls.append(i)
  
  def __repr__(self):
    return f"{self.ls}"

class Matrix:
  res = ""
  def __init__(self, *args):
    self.data = args
    self.ls = []
    for i in self.data:
      if not isinstance(i, list):
        raise TypeError("Type must be list...")
      if len(i) != 2:
        raise TypeError("Length of list must be 2...")
      self.res += f"{i}\n"
  
  def __repr__(self):
    return self.res
  
vec = Vector(1, 2, 3, 4)
print(vec)

matrix = Matrix([1, 2], [3, 4])
print(matrix)