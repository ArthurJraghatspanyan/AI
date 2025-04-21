# Implementing zip

import typing

def custom_zip(*iterables):
  res = []
  min_len = len(min(iterables, key=len))
  for i in range(min_len):
    tmp = []
    for iter in iterables:
      if not isinstance(iter, typing.Iterable):
        raise TypeError("Object must be iterable")
      tmp.append(iter[i])
    res.append(tuple(tmp))
  return res

print(custom_zip([1, 2, 3], ['a', 'b', 'c']))