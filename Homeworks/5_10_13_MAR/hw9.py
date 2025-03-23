# Write a function is_even that takes a number and returns True if the number is even and False otherwise.
# print(is_even(4)) # True
# print(is_even(5)) # False

def is_even(num):
  if num % 2 == 0:
    return True
  return False

print(is_even(4))
print(is_even(5))