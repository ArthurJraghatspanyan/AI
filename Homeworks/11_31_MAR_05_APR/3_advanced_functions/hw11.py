# Implement custom_enumerate using yield, similar to the Python built-in enumerate.

import typing

def custom_enumerate(iterable, start=0):
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Type must be iterable.")
  if not isinstance(start, int):
    raise TypeError("Type must be integer.")
  for i in iterable:
    yield start, i
    start += 1


ls = ["Good", "Morning", "Welcome"]
print(list(custom_enumerate(ls, 100)))