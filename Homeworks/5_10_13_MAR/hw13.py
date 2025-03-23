# Write a function count_digits that takes an integer and returns the number of digits in it.
# print(count_digits(12345))  # Example call

def count_digits(num):
  if not isinstance(num, int):
    return "Error: Number must be integer"
  num_str = str(num)
  num_of_digits = 0
  for i in range(len(num_str)):
    num_of_digits += 1
  return num_of_digits

print(count_digits(12345))