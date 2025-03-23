# Write a function make_accumulator(start=0) that returns a function which adds its argument to start and returns the new total each time it is called.

def make_accumulator(start=0):
  total = 0
  def inner(num):
    nonlocal total
    total += num + start
    return total
  return inner

result = make_accumulator()
print(result(5))
print(result(10))
print(result(15))