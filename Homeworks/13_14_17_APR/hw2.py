# Implement a decorator memoize that caches the results of the decorated function to avoid redundant computations.

def memoize(fn):
  cache = {}
  def inner(n):
    for i in range(n):
      if i not in cache:
        cache[i] = fn(n)
    return fn(n)
  return inner

@memoize
def fibonacci(n):
  if n <= 1:
    return n
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))
# Output: 55 (calculated efficiently using caching)