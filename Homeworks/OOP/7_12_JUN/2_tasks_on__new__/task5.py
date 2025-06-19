# Task 5: Custom Immutable Object

class ImmutablePoint(tuple):
  def __new__(cls, x, y):
    if not isinstance(x, int) or not isinstance(y, int):
      raise TypeError("Elements must be integer type...")
    return tuple.__new__(cls, (x, y))
  
  def __setattr__(self):
    raise TypeError("")

obj = ImmutablePoint(1, 2)
print(obj)
print(obj[0])
print(obj[1])
obj[1] = 10     # TypeError: Tuple is immutable