# Implement a decorator time_it that measures the time taken by a function to execute and prints it.
# Apply this decorator to a function that calculates the sum of squares of numbers from 1 to 1000.

import time

def time_it(fn):
  def inner(*args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)
    end = time.time()
    print(f"Time of completing the function {fn.__name__} is: {(end - start):.10f}")
    return fn(*args, **kwargs)
  return inner

@time_it
def sum_of_squares():
  summ = 0
  for i in range(1, 1001):
    summ += i ** 2
  return summ

sum_of_squares()