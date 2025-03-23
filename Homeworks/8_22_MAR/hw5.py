# Sum of Natural Numbers
# Create a recursive function to find the sum of the first n natural numbers.

def sum_natural(n):
  if n == 0:
    return 0
  return n + sum_natural(n - 1)

print(sum_natural(10))