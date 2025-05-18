# Write a function calculate_average that takes any number of numerical arguments and returns their average.

def calculate_average(*args):
  sum = 0
  if len(args) == 0:
    return 0
  for i in args:
    if not isinstance(i, int):
      raise TypeError("Type must be integer.")
  if len(args) == 1:
    return args[0]
  for i in args:
    sum += i
  return f"Average is: {sum / len(args)}"

print(calculate_average(1, 3, 5, 2, 56, 12, 4142))