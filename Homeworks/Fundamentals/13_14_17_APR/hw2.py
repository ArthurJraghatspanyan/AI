# Implement a decorator memoize that caches the results of the decorated function to avoid redundant computations.

def memoize(fn):
  cache = {}
  def inner(*args, **kwargs):
    key = (args, tuple(sorted(kwargs)))
    if key not in cache:
      cache[key] = fn(*args, **kwargs)
    return cache[key]
  return inner

@memoize
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# Output: 55 (calculated efficiently using caching)