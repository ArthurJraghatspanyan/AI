# Write a function fibonacci(n) that calculates the nth Fibonacci number without using recursion.
# Use an iterative approach to compute the result.

def fibonacci(n):
  fib_numbers = [1, 1]
  fib_index = 2
  if n <= 0:
    return 0
  elif n == 1 or n == 2:
    return 1
  while fib_index < n:
    fib_numbers.append((fib_numbers[len(fib_numbers) - 1]) + (fib_numbers[len(fib_numbers) - 2]))
    fib_index += 1
  return fib_numbers[n - 1]

print(fibonacci(9))