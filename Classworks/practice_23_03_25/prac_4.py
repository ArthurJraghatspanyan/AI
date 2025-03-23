# Write a Python function chain_sum that allows numbers to be added sequentially by calling the function multiple times,
# each time passing a number. The function should return itself when a number is provided, allowing an indefinite chain of calls.
# When called without arguments, it should return the accumulated sum.

def chain_sum():
  sum = 0
  def inner(n=0):
    nonlocal sum
    if n:
      sum += n
      return inner
    return sum
  return inner

print(chain_sum()(1)(2)(3)(4)())
print(chain_sum()(5)(10)(-2)())
print(chain_sum()(100)())
print(chain_sum()())