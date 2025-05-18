# Implementing map
# Task: Write a Python function named custom_map that replicates the behavior of the built-in map function.

import typing

def custom_map(fn, *iterables):
  if not isinstance(fn, typing.Callable):
    raise TypeError("The bject must be callable")
  res = []
  min_len = len(min(iterables, key=len))
  for i in range(min_len):
    tmp = []
    for iter in iterables:
      if not isinstance(iterables, typing.Iterable):
        raise TypeError("The bject must be iterable")
      tmp.append(iter[i])
    res.append(fn(*tmp))

  return res

res = custom_map(lambda x: x ** 2, [1, 2, 3, 4, 5, 6])
print(list(res))