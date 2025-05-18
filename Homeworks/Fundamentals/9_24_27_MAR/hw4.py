# Implementing reduce

import typing

def custom_reduce(fn, iterable, initial=None):
  if not callable(fn):
    raise TypeError("Object must be Callable")
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Object must be iterable")
  if not iterable:
    if initial == None:
      raise ValueError("At least initial must be provided")
    return initial
  if initial != None:
    res = initial
    start = 0
  else:
    res = iterable[0]
    start = 1
  for i in range(start, len(iterable)):
    res = fn(res, iterable[i])

  return res

print(custom_reduce(lambda x, y: x + y, [1, 2, 3, 4, 5], 4))