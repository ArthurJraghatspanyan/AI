# Write a function sum_numbers that accepts an arbitrary number of positional arguments and returns their sum.
# Call the function with three numbers.
# Call the function with no arguments and ensure it handles this case gracefully.

def sum_numbers(*args):
  summary = 0
  for i in args:
    summary += i
  return summary

print(sum_numbers(1, 2, 3))
print(sum_numbers())