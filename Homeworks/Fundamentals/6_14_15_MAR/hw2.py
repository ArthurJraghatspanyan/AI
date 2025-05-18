# Write a function factorial(n) that calculates the factorial of a given number using an iterative approach.

def factorial(n):
  factorial_ls = [1, 2]
  mul = 1
  if n < 0:
    return 0
  elif n == 0 or n == 1:
    return 1
  fac = 3
  while fac <= n:
    factorial_ls.append(mul * fac * factorial_ls[fac - 2])
    fac += 1
  return factorial_ls[fac - 2]

print(factorial(7))