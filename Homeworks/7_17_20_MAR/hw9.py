# Write a closure that tracks the number of times a specific function is called.

def outter():
  counter = 0
  def inner():
    nonlocal counter;
    counter += 1
    return f"Function called {counter} times."
  return inner

closure = outter()
print(closure())
print(closure())
print(closure())
