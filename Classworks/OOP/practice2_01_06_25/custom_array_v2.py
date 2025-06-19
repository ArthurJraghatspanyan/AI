# Assignment — CustomArray v2: Mastering @property

class CustomArray:
  def __init__(self, data: list, dtype: str):
    if not isinstance(data, list):
      raise TypeError("Data must be List.")
    if not data:
      raise ValueError("Data must not be empty.")
    if not isinstance(dtype, str):
      raise TypeError("Data Type must be string.")
    if not dtype:
      raise ValueError("Data type must not be empty.")
    for i in range(len(data)):
      if dtype.lower() == "int":
        data[i] = int(data[i])
      elif dtype.lower() == "float":
        data[i] = float(data[i])
      elif dtype.lower() == "str":
        data[i] = str(data[i])
      else:
        raise ValueError("No such data type to parse.")

    self._data = data
    self._dtype = dtype
  
  @property
  def data(self):
    return self._data
  
  @property
  def dtype(self):
    return self._dtype
  
  @dtype.setter
  def dtype(self, newDtype: str):
    if not isinstance(newDtype, str):
      raise TypeError("Data Type must be string.")
    if not newDtype:
      raise ValueError("Data type must not be empty.")
    if newDtype != "int" and newDtype != "float" and newDtype != "str":
      raise ValueError(f"Data type must be int, float or str.")
    for i in range(len(self._data)):
      if newDtype == "int":
        self._data[i] = int(self._data[i])
      elif newDtype == "float":
        self._data[i] = float(self._data[i])
      elif newDtype == "str":
        self._data[i] = str(self._data[i])
    self._dtype = newDtype
  
  @property
  def shape(self):
    return (len(self._data),)
  
  @property
  def size(self):
    return len(self._data)
  
  @property
  def is_numeric(self):
    if self._dtype == "int" or self._dtype == "float":
      return True
    return False
  
  @property
  def mean(self):
    if self._dtype == "str":    # String can not be counted in mean.
      raise TypeError("Can't count mean of data which type is string.")
    return sum(self._data) / len(self._data)
  
  def __add__(self, other: list):
    if isinstance(other, int):
      return self.__radd__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Data must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Length of two datas must be same.")
    return CustomArray([self._data[i] + other._data[i] for i in range(len(self._data))], dtype=self._dtype)
  
  def __sub__(self, other: list):
    if isinstance(other, int):
      return self.__rsub__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Data must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Length of two datas must be same.")
    return CustomArray([self._data[i] - other._data[i] for i in range(len(self._data))], dtype=self._dtype)
  
  def __mul__(self, other: list):
    if isinstance(other, int):
      return self.__rmul__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Data must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Length of two datas must be same.")
    return CustomArray([self._data[i] * other._data[i] for i in range(len(self._data))], dtype=self._dtype)
  
  def __truediv__(self, other: list):
    if isinstance(other, int):
      return self.__rtruediv__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Data must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Length of two datas must be same.")
    try:
      res = CustomArray([self._data[i] / other._data[i] for i in range(len(self._data))], dtype=self._dtype)
      return res
    except ZeroDivisionError as e:
      raise e
    
  def __floordiv__(self, other: list):
    if isinstance(other, int):
      return self.__floordiv__(other)
    if not isinstance(other, CustomArray):
      raise TypeError("Data must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Length of two datas must be same.")
    try:
      res = CustomArray([self._data[i] // other._data[i] for i in range(len(self._data))], dtype=self._dtype)
      return res
    except ZeroDivisionError as e:
      raise e
  
  def __radd__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Other type must be int.")
    return CustomArray([self._data[i] + other for i in range(len(self._data))], dtype=self._dtype)
  
  def __rsub__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Other type must be int.")
    return CustomArray([self._data[i] - other for i in range(len(self._data))], dtype=self._dtype)
  
  def __rmul__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Other type must be int.")
    return CustomArray([self._data[i] * other for i in range(len(self._data))], dtype=self._dtype)
  
  def __rtruediv__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Other type must be int.")
    try:
      res = CustomArray([self._data[i] / other for i in range(len(self._data))], dtype=self._dtype)
      return res
    except ZeroDivisionError as e:
      raise e
  
  def __rfloordiv__(self, other: int):
    if not isinstance(other, int):
      raise TypeError("Other type must be int.")
    try:
      res = CustomArray([self._data[i] // other for i in range(len(self._data))], dtype=self._dtype)
      return res
    except ZeroDivisionError as e:
      raise e
  
  def __matmul__(self, other: list):
    if not isinstance(other, CustomArray):
      raise TypeError("Object type must be CustomArray.")
    if len(self._data) != len(other._data):
      raise ValueError("Lengths of CustomArrays must be same")
    res = 0
    for i in range(len(self._data)):
      res += self._data[i] * other._data[i]
    return res
  
  def __setitem__(self, position: int, value):    # For inplace assignment
    if not isinstance(position, int):
      raise TypeError("Assignment value must be int.")
    self._data[position] = value

# --- construction ---
a = CustomArray([1, 2, 3], dtype="int")   # default dtype is "int"

assert a.data       == [1, 2, 3]    # copy, not the real list
assert a.dtype      == "int"
assert a.shape      == (3,)
assert a.size       == 3
assert a.is_numeric is True
assert a.mean       == 2            # arithmetic mean

# --- dtype *setter* must convert *in-place* ---
a.dtype = "float"
assert a.data == [1.0, 2.0, 3.0]
try:
  a.dtype = "float"
except ValueError as e:
  raise e

# --- element-wise arithmetic with scalar broadcasting ---
b = CustomArray([4, 5, 6], dtype="float")
assert (a + b).data == [5.0, 7.0, 9.0]
assert (a * 2).data == [2.0, 4.0, 6.0]

# --- dot product with @ (numeric, equal length) ---
assert a @ b == 32.0

# --- BONUS: in-place assignment using [] ---
a[1] = 10
assert a.data == [1.0, 10.0, 3.0]

# --- strings have no mean ---
c = CustomArray(["x", "y"], "str")
try:
  _ = c.mean
except TypeError as e:
  raise e