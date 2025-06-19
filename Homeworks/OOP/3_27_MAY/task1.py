# TASK 1: Vector Class with Operator Overloading for Addition and Subtraction

class Vector:
  def __init__(self, data: list):
    if not isinstance(data, list):
      raise TypeError("Type must be List.")
    if not data:
      raise ValueError("Data must have one or more elements.")
    self.data = data
  def __add__(self, other: list):
    if not isinstance(other, Vector):
      raise TypeError("Type must be Vector.")
    if len(self.data) != len(other.data):
      raise ValueError("Length of vectors must be same.")
    return Vector([self.data[i] + other.data[i] for i in range(len(self.data))])
  def __sub__(self, other: list):
    if not isinstance(other, Vector):
      raise TypeError("Type must be Vector.")
    if len(self.data) != len(other.data):
      raise ValueError("Length of vectors must be same.")
    return Vector([self.data[i] - other.data[i] for i in range(len(self.data))])
  
  def __repr__(self):
    return f"{self.data}"

v1 = Vector([4, 5, 6])
v2 = Vector([1, 2, 3])

print(v1 + v2)
print(v1 - v2)