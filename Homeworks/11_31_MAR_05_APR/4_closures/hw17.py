# Create a closure that takes a multiplier as an argument and returns a function that multiplies
# any given number by that multiplier.

def multiply_closure(multiplier):
  if not isinstance(multiplier, int):
      raise TypeError("Type must be integer")
  def inner(num):
    if not isinstance(num, int):
      raise TypeError("Type must be integer")
    return num * multiplier
  return inner

closure = multiply_closure(3)
print(closure(8))