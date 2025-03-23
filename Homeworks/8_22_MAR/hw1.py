# Write a function print_down_from_n(n) that prints numbers from n to 1 using recursion.

def print_down_from_n(n):
  if n <= 1:
    return n
  print(n)
  return print_down_from_n(n - 1)

print(print_down_from_n(10))