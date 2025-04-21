# Implement custom_filter_with_yield that yields items from an iterable that satisfy a given condition.

import typing

def custom_filter_with_yield(func, iterable):
  if not isinstance(func, typing.Callable) and func != None:
    raise TypeError("Function must be callable")
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Type must be iterable")
  if func == None:
    func = lambda x: x
  for i in iterable:
    if func(i):
      yield i

print(list(filter(None, [1, 2, 3, 4, 0, 5, 6])))
print(list(custom_filter_with_yield(None, [1, 2, 3, 4, 0, 5, 6])))