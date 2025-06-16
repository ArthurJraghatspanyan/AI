# TASK 6: Overload == Operator to Compare Vector or Matrix Equality

class Vector:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List...")
    for i in data:
      if not isinstance(i, int):
        raise TypeError("Type must be Integer...")
    self.data = data
  
  def __eq__(self, other: list):
    if not isinstance(other, Vector):
      raise TypeError("Vector must be Vector type...")
    if len(self.data) != len(other.data):
      raise ValueError("Length of two vectors must be same")
    for i in range(len(self.data)):
      if self.data[i] == other.data[i]:
        flag = True
      else:
        flag = False
    return flag

class Matrix:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List...")
    for i in data:
      if not isinstance(i, list):
        raise TypeError("Type must be List...")
      for j in i:
        if not isinstance(j, int):
          raise TypeError("Type must be Integer...")
    self.data = data
  
  def __eq__(self, other: list):
    if not isinstance(other, Matrix):
      raise TypeError("Matrix must be Matrix type...")
    if len(self.data) != len(other.data):
      raise ValueError("Lengths must be same")
    for i in range(len(self.data)):
      if len(self.data[i]) != len(other.data[i]):
        raise ValueError("Lengths must be same")
      for j in range(len(self.data[i])):
        if self.data[i][j] == other.data[i][j]:
          flag = True
        else:
          flag = False
    return flag


vec1 = Vector([1, 2, 3])
vec2 = Vector([1, 2, 3])

print(vec1 == vec2)

mat1 = Matrix([[1, 2], [3, 4]])
mat2 = Matrix([[1, 2], [3, 4]])

print(mat1 == mat2)