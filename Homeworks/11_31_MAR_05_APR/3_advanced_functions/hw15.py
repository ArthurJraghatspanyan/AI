# Write a zip_generator that takes multiple iterables and yields tuples, similar to Python’s zip.

import typing

def zip_generator(*iterables):
  if not isinstance(iterables, typing.Iterable):
    raise TypeError("Type must be iterable")
  min_len = len(min(iterables, key=len))
  for i in range(min_len):
    tmp = []
    for iterable in iterables:
      tmp.append(iterable[i])
    yield tuple(tmp)

print(list(zip([1, 2, 3, 4, 5], ["Hello", "World", "Python", "Zip"], [100, 200, 300, 400, 500])))
print(list(zip_generator([1, 2, 3, 4, 5], ["Hello", "World", "Python", "Zip"], [100, 200, 300, 400, 500])))