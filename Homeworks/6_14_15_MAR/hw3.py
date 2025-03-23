# Write a function is_prime(n) that checks if a number is a prime number using a loop.
# The function should return True if the number is prime and False otherwise.

def is_prime(n):
  if n < 3:
    return True
  elif n % 2 == 0:
    return False
  return True

print(is_prime(17))