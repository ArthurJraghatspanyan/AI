# Implementing enumerate

import typing

def custom_enumerate(iterable, start=0):
  if not isinstance(iterable, typing.Iterable):
    raise TypeError
  res = []
  for i in range(len(iterable)):
    res.append((start, iterable[i]))
    start += 1  
  return res

print(list(custom_enumerate([1, 2, 3, 4])))