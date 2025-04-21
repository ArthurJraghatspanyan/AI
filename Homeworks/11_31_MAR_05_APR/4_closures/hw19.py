# Create a closure to calculate running totals. Each call to the inner function should add a number to the total
# and return the updated total.

def totals():
  total = 0
  def inner(num=0):
    nonlocal total
    if num:
      total += num
      return inner
    return total
  return inner

print(totals()(4)(2)(5)(1)())
print(totals()())