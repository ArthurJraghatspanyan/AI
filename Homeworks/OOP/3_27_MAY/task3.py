# TASK 3: Polymorphic Determinant Calculation

"""
We use Polymorphism here to avoid code repetition for higher shape matrixes
It helps to write specific logic for specific shape matrix in one Class.
"""

class SquareMatrix:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List.")
    self.data = data

  def determinant(self):
    pass

class Matrix2x2:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List.")
    self.data = data

  def determinant(self):
    if not isinstance(self.data, list):
      raise TypeError("Type must be List")
    if len(self.data) != 2:
      raise ValueError("Matrix must contain 2 rows and columns...")
    for i in self.data:
      if not isinstance(i, list):
        raise TypeError("Type must be List...")
      if len(i) != 2:
        raise ValueError("Elements' length must be two...")
      for j in i:
        if not isinstance(j, int):
          raise TypeError("Type of element must be integer...")
    return (self.data[0][0] * self.data[1][1]) - (self.data[0][1] * self.data[1][0])

class Matrix3x3:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List.")
    self.data = data

  def determinant(self):
    if not isinstance(self.data, list):
      raise TypeError("Type must be List")
    if len(self.data) != 3:
      raise ValueError("Matrix must contain 2 rows and columns...")
    for i in self.data:
      if not isinstance(i, list):
        raise TypeError("Type must be List...")
      if len(i) != 3:
        raise ValueError("Elements' length must be two...")
      for j in i:
        if not isinstance(j, int):
          raise TypeError("Type of element must be integer...")
    a = self.data[0][0] * self.data[1][1] * self.data[2][2]
    b = self.data[0][1] * self.data[1][2] * self.data[2][0]
    c = self.data[0][2] * self.data[1][0] * self.data[2][1]
    d = self.data[0][2] * self.data[1][1] * self.data[2][0]
    e = self.data[0][1] * self.data[1][0] * self.data[2][2]
    f = self.data[0][0] * self.data[1][2] * self.data[2][1]
    return a + b + c - d - e - f

ls = [Matrix2x2([[1, 2], [3, 4]]),
      Matrix3x3([[5, 15, 3], [-4, 1, 9], [11, -8, 6]])]

for i in ls:
  print(i.determinant())