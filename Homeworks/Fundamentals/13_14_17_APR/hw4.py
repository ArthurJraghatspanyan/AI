# Create a decorator run_once that ensures a function can only be executed once.
# On subsequent calls, it should print a message indicating that the function has already been executed.
# Test it on a function that initializes a resource.

def run_once(fn):
  flag = False
  def inner(*args, **kwargs):
    nonlocal flag
    if flag:
      raise RuntimeError("Function has already been executed")
    flag = True
    return fn(*args, **kwargs)
  return inner

@run_once
def add(x, y):
  print(x + y)

add(5, 7)
add(5, 7)