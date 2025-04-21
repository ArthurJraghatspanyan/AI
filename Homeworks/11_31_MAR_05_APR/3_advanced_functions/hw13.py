# Create a function custom_map_with_yield that applies a transformation to elements of an iterable and yields each result.

import typing

def custom_map_with_yield(func, *iterables):
  if not callable(func):
    raise TypeError("Function must be callable")
  if not isinstance(iterables, typing.Iterable):
    raise TypeError("Type must be iterable")
  min_len = len(min(iterables, key=len))
  for i in range(min_len):
    tmp = []
    for iterable in iterables:
      tmp.append(iterable[i])
    yield func(*tmp)

print(list(map(lambda x, y, z: x * y * z, [1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5])))
print(list(custom_map_with_yield(lambda x, y, z: x * y * z, [1, 2, 3, 4, 5], [1, 2, 3, 4], [1, 2, 3, 4, 5])))