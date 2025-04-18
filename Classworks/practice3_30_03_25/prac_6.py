# Implement custom_enumerate using yield, similar to the Python built-in enumerate.

def custom_enumerate(iterable, start=0):
  for i in iterable:
    yield (start, i)
    start += 1

print(list(enumerate([1, 2, 3, 4], 5)))
print(list(custom_enumerate([1, 2, 3, 4], 5)))