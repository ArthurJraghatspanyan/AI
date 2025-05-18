# Write a function find_max that takes two numbers and returns the larger of the two.
# print(find_max(10, 20))  # Example call

def find_max(num1: int, num2: int):
  if num1 > num2:
    return num1
  elif num2 > num1:
    return num2
  else:
    return "Both are equal"

print(find_max(10, 20))