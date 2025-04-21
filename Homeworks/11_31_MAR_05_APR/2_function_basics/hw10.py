# Write a function divide_numbers that accepts two numbers and returns their division result.
# Add error handling for division by zero.

def divide_numbers(x, y):
  if y == 0:
    raise ValueError("Division by 0 is impossible.")
  return x / y

print(divide_numbers(10, 4))