# Write a closure that creates a counter. Each call to the inner function should increment the counter by 1 and return the current count.

def outter():
  counter = 0
  def inner():
    nonlocal counter;
    counter += 1
    return counter
  return inner

closure = outter()
print(f"1: {closure()}")
print(f"2: {closure()}")
print(f"3: {closure()}")