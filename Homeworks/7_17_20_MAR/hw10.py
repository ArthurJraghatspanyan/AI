# Create a closure to calculate running totals. Each call to the inner function should add a number to the total and return the updated total.

def outter():
  total = 0
  def inner(num):
    nonlocal total;
    total += num
    return total
  return inner

closure = outter()
print(closure(5))
print(closure(8))
print(closure(10))