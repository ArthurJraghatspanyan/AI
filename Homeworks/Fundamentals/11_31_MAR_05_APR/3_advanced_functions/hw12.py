# Write a generator function range_generator that mimics the behavior of range(start, stop, step) using yield.

def range_generator(start, stop=None, step=1):
  if stop == None:
    stop = start
    start = 0
  if not isinstance(start, int) and not isinstance(stop, int) and not isinstance(step, int):
    raise TypeError("Type of at least one argument must be int")
  while start < stop:
    yield start
    start += step

print(list(range_generator(11)))
print(list(range(11)))