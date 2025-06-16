# TASK 7: Scalar Multiplication via * Operator

class Vector:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List...")
    for i in data:
      if not isinstance(i, int):
        raise TypeError("Type must be Integer...")
    self.data = data
  
  def __mul__(self, other):
    if isinstance(other, int):
      return self.__rmul__(other)
    if not isinstance(other, Vector):
      raise TypeError("Object type must be Vector")
    if len(self.data) != len(other.data):
      raise ValueError("Lengths of Vectors must be same")
    return [self.data[i] * other.data[i] for i in range(len(self.data))]

  def __rmul__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    return [self.data[i] * other for i in range(len(self.data))]


class Matrix:
  def __init__(self, data: list):
    if not isinstance(data, list):
        raise TypeError("Type must be List...")
    for i in data:
      if not isinstance(i, list):
        raise TypeError("Type must be List...")
      for j in i:
        if not isinstance(j, int):
          raise TypeError("Type must be integer...")
    self.data = data
  
  def __mul__(self, other):
    if isinstance(other, int):
      return self.__rmul__(other)
    if not isinstance(other, Matrix):
      raise TypeError("Object type must be Vector")
    if len(self.data) != len(other.data):
      raise ValueError("Lengths of Vectors must be same")
    res = []
    for i in range(len(self.data)):
      tmp = []
      if len(self.data[i]) != len(other.data[i]):
        raise ValueError("Lengths of Matrixes must be same")
      for j in range(len(self.data[i])):
        tmp.append(self.data[i][j] * other.data[i][j])
      res.append(tmp)
    return res
  
  def __rmul__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    res = []
    for i in range(len(self.data)):
      tmp = []
      for j in range(len(self.data[i])):
        tmp.append(self.data[i][j] * other)
      res.append(tmp)
    return res
      

vec1 = Vector([1, 2, 3])
vec2 = Vector([4, 5, 6])

print(vec1 * vec2)
print(vec1 * 3)
print(4 * vec2)

print()

mat1 = Matrix([[1, 2, 3], [4, 5, 6]])
mat2 = Matrix([[7, 8, 9], [10, 11, 12]])

print(mat1 * mat2)
print(mat1 * 14)
print(12 * mat2)