# Write a decorator memoize that caches function results in a dictionary based on the input arguments.

def memorize(fn):
  cache = {}
  def inner(*args, **kwargs):
    nonlocal cache
    dict_value = [i for i in kwargs.values()]
    cache[(*args, *dict_value)] = fn(*args, **kwargs)
    print(cache)
  return inner

def data(a, b, c):
  return a + b + c

res = memorize(data)
res(4, 6, c = 5)