# Create a closure that takes a multiplier as an argument and returns a function that multiplies any given number by that multiplier.

def multiply(mul):
  def inner(operand):
    return operand * mul
  return inner

closure = multiply(3)
print(closure(4))
print(closure(6))
print(closure(8))