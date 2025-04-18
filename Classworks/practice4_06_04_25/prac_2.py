# Write a generator function prime_generator(n) that yields prime numbers up to n.
# Use this generator to print all prime numbers less than 100

def prime_generator(n):
  for i in range(2, n):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
      if i % j == 0:
        is_prime = False
    if is_prime:
      yield i

print(list(prime_generator(100)))