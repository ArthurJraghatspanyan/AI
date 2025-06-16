# Task 5: Custom Immutable Object

class ImmutablePoint(tuple):
  def __new__(cls, x, y):
    return tuple.__new__(cls, (x, y))
  
  def __setattr__(self):
    raise TypeError("")

obj = ImmutablePoint(1, 2)

print(obj[0])
print(obj[1])
obj[1] = 10     # TypeError: Tuple is immutable