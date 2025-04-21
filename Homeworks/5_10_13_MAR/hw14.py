# Write a function sum_of_digits that calculates the sum of all digits in an integer
# print(sum_of_digits(123))  # Example call

def sum_of_digits(num):
  if not isinstance(num, int):
    return "Error: Number must be integer"
  sum = 0
  while num != 0:
    sum += num % 10
    num //= 10
  return sum

print(sum_of_digits(123))