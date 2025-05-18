# 1. Implementing filter
# Task: Write a Python function named custom_filter that replicates the behavior of the built-in filter function.

import typing

def custom_filter(fn, iterable):
  res = []
  if fn is not None and not isinstance(fn, typing.Callable):
    raise TypeError("This object is not callable.")
  if fn is not None and not isinstance(iterable, typing.Iterable):
    raise TypeError("This object is not iterable.")
  if fn is None:
    for i in iterable:
      if i:
        res.append(i)
  if fn:
    for i in iterable:
      if fn(i):
        res.append(i)
  return res

print(custom_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))