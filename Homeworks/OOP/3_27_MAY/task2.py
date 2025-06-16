# TASK 2: Matrix Class with @ Operator for Multiplication

class Matrix:
  def __init__(self, data: list[list]):
    if not isinstance(data, list):
      raise TypeError("Type must be List.")
    if len(data) != 2:
      raise ValueError("Length must be 2.")
    for i in data:
      if not isinstance(i, list):
        raise TypeError("Type must be List.")
      if len(i) != 2:
        raise ValueError("Length must be 2.")
    self.data = data

  def __matmul__(self, other: list[list]):
    if not isinstance(other, Matrix):
      raise TypeError("Type must be Matrix.")
    res = 0
    for i in range(len(self.data)):
      for j in range(len(self.data[i])):
        res += self.data[i][j] * other.data[i][j]
    return res

v1 = Matrix([[1, 2], [3, 4]])
v2 = Matrix([[5, 6], [7, 8]])

print(v1 @ v2)