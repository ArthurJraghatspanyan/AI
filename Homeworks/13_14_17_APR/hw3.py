# Create a decorator delay that delays the execution of the decorated function by n seconds, where n is provided
# as an argument.

import time

def delay(n):
  def decorator(fn):
    def inner():
      print("Waiting for 3 seconds...")
      time.sleep(n)
      fn()
      return fn
    return inner
  return decorator

@delay(3)
def say_hello():
  print("Hello, World!")

say_hello()

# Output:
# Waiting for 3 seconds...
# Hello, World!