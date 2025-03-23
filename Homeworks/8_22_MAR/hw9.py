# Power of a Number
# Write a recursive function to calculate the power of a number x raised to n.
# For example, 2^4 means multiplying 2 by itself 4 times: 2 * 2 * 2 * 2 = 16.

def power(x, n):
  if n == 0:
    return 1
  return x * power(x, n - 1)

print(power(3, 3))