# Write a function is_prime(n) that checks if a number is a prime number using a loop.
# The function should return True if the number is prime and False otherwise.

def is_prime(n):
  if n <= 1:
    return False
  flag = True
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      flag = False
  return flag

print(is_prime(13))