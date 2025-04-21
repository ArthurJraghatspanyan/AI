# Write a decorator execution_timer that measures and prints the time taken by the decorated function to execute.

import time

def execution_timer(fn):
  def inner(*args, **kwargs):
    start = time.time()
    fn(*args, **kwargs)
    end = time.time()
    print(f"{fn.__name__} took {end - start:.2f} seconds to execute.")
  return inner

@execution_timer 
def slow_function(): 
  time.sleep(2)
  print("Finished execution!")

slow_function()

# Output:
# Finished execution!
# slow_function took 2.00 seconds to execute.