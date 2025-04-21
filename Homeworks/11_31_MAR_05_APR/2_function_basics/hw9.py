# Create a function all_greater that takes a list and a number as arguments and checks if all elements
# in the list are greater than the number.

import typing

def all_greater(ls, num):
  if not isinstance(ls, typing.Iterable):
    raise TypeError("Type must be iterable.")
  if not isinstance(num, int):
    raise TypeError("Type must be integer.")
  for i in ls:
    if not isinstance(i, int):
      raise TypeError("Type must be integer.")
    if i <= num:
      return False
    return True

ls = [1, 4, 2, 5, 8, 2, 10]
print(all_greater(ls, -2))