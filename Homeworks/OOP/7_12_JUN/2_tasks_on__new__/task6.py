# Task 6: Subclassing an Immutable Type

class CustomTuple(tuple):
  def __new__(cls, *args, **kwargs):
    for i in args:
      if not isinstance(i, int):
        raise TypeError("Type of args values must be integer...")
    for j in kwargs:
      if not isinstance(kwargs[j], int):
        raise TypeError("Type of kwargs values must be integer...")
    dict_values = [i for i in kwargs.values()]
    return tuple.__new__(cls, (args + tuple(sorted(dict_values))))

custom = CustomTuple(1, 2, 3, b=4)
print(custom)

custom2 = CustomTuple(1, "x")     # TypeError