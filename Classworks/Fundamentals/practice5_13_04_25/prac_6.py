# # Implement a memoization decorator memoize that caches the results of a function to improve performance.
# # Apply this decorator to a recursive function that computes the Fibonacci sequence.
# # Demonstrate the speed improvement by calling the decorated function multiple times.

import time

def memoize(fn):
  cache = {}
  def inner(*args, **kwargs):
    nonlocal cache
    key = (args, tuple(sorted(kwargs)))
    if key not in cache:
      cache[key] = fn(*args, **kwargs)
    return cache[key]
  return inner

def time_dec(fn):
  def inner(*args, **kwargs):
    start = time.time()
    res = fn(*args, **kwargs)
    end = time.time()
    print(f"Time is: {(end - start):.10f}")
    return res
  return inner

@memoize
def wrapper_memoize(num):
  return fibonacci_rec(num)

@time_dec
def wrapper_timer(num):
  fibonacci_rec(num)

def fibonacci_rec(n):
  if n <= 1:
    return n
  return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)

num = 10

print(wrapper_memoize(num))

wrapper_timer(num)
wrapper_timer(num)
wrapper_timer(num)