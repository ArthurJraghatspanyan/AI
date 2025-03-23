# Fibonacci Sequence
# Write a recursive function to calculate the nth Fibonacci number.
# The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
# For example, the sequence begins as 0, 1, 1, 2, 3, 5, 8....

def fibonacci(n):
  if n == 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(5))