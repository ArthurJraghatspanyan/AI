# Implement a recursive function which will calculate the gcd of two numbers.

def gcd(x, y):
  if y == 0:
    return x
  else:
    return gcd(y, x % y)

print(gcd(16, 4))