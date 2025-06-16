import typing

class CustomArray:
  def __init__(self, data: list, dtype: str = "int"):
    if not isinstance(data, typing.List):
      raise TypeError("Data type must be List.")
    if not isinstance(dtype, str):
      raise TypeError("Data Type must be string.")
    for i in range(len(data)):
      if dtype == "int":
        data[i] = int(data[i])
      elif dtype == "float":
        data[i] = float(data[i])
      elif dtype == "str":
        data[i] = str(data[i])
      else:
        raise ValueError("Data must be int, float or str.")
    self.__data = data
    self.__dtype = dtype
  
  def __add__(self, other):
    if isinstance(other, int):
      return self.__radd__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    return CustomArray([self.__data[i] + other.__data[i] for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __sub__(self, other):
    if isinstance(other, int):
      return self.__rsub__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    return CustomArray([self.__data[i] - other.__data[i] for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __mul__(self, other):
    if isinstance(other, int):
      return self.__rmul__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    return CustomArray([self.__data[i] * other.__data[i] for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __truediv__(self, other):
    if isinstance(other, int):
      return self.__rtruediv__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    try:
      return CustomArray([self.__data[i] / other.__data[i] for i in range(len(self.__data))], dtype=self.__dtype)
    except ZeroDivisionError as e:
      raise e

  def __floordiv__(self, other):
    if isinstance(other, int):
      return self.__rfloordiv__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    try:
      return CustomArray([self.__data[i] // other.__data[i] for i in range(len(self.__data))], dtype=self.__dtype)
    except ZeroDivisionError as e:
      raise e
    
  def __radd__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    return CustomArray([self.__data[i] + other for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __rsub__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    return CustomArray([self.__data[i] - other for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __rmul__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    return CustomArray([self.__data[i] * other for i in range(len(self.__data))], dtype=self.__dtype)
  
  def __rtruediv__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    try:
      return CustomArray([self.__data[i] / other for i in range(len(self.__data))], dtype=self.__dtype)
    except ZeroDivisionError as e:
      raise e
  
  def __rfloordiv__(self, other):
    if not isinstance(other, int):
      raise TypeError("Object type must be integer.")
    try:
      return CustomArray([self.__data[i] // other for i in range(len(self.__data))], dtype=self.__dtype)
    except ZeroDivisionError as e:
      raise e
  
  def __matmul__(self, other):
    if not isinstance(other, CustomArray) or not isinstance(self, CustomArray):
      raise TypeError("Object type must be CustomArray.")
    if (self.__data == "str" and other.__data == "str") or (self.__data == "str" and other.__data == "str"):
      raise TypeError("Data type must be int or float.")
    if len(self.__data) != len(other.__data):
      raise ValueError("Lengths of CustomArrays must be same")
    res = 0
    for i in range(len(self.__data)):
      res += self.__data[i] * other.__data[i]
    return res
  
  def to_list(self):
    return self.__data
  
  def get_dtype(self):
    return self.__dtype
  
  def astype(self, new_dt: str):
    for i in range(len(self.__data)):
      if new_dt == "int":
        self.__data[i] = int(self.__data[i])
      elif new_dt == "float":
        self.__data[i] = float(self.__data[i])
      elif new_dt == "str":
        self.__data[i] = float(self.__data[i])
      else:
        raise ValueError("Data must be int, float or str.")
    return CustomArray(self.__data, dtype=new_dt)
  
  def shape(self):
    return (len(self.__data),)
  
  def __repr__(self):
    return f"CustomArray({self.__data}, dtype={self.__dtype})"

a = CustomArray([1, 2, 3], dtype="float")
b = CustomArray([4, 5, 6], dtype="float")

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a / b)

print(a + 10)
print(a - 10)
print(a * 10)
print(a // 10)
print(a / 10)

print(a @ b)
print(b @ a)

print(a.to_list())
print(a.get_dtype())
c = a.astype("int")
print(c)

print(a.shape())