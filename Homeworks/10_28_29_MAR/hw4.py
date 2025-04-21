# Fibonacci Generator (Intermediate)
# Objective
  # Introduce a slightly more complex logic to generate a well-known sequence.
  # Reinforce lazy evaluation: only generate the next Fibonacci number upon request.
# Task
  # Write a generator function fibonacci(limit=None) that yields Fibonacci numbers.
  # If limit is not given (None), generate an infinite sequence. Otherwise, stop once the next Fibonacci number would exceed the limit.
  # Demonstrate by printing the first 10 Fibonacci numbers (or all Fibonacci numbers up to a certain limit if provided).

def fibonacci(limit=None):
  a, b = 0, 1
  if limit != None and not isinstance(limit, int):
    raise TypeError("Limit must be integer type")
  elif limit == None:
    while True:
      yield a
      a, b = b, a + b
  elif limit != None:
    for _ in range(limit):
      yield a
      a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
  print(next(fib_gen))

print()

for num in fibonacci(limit=100):
  print(num)