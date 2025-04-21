# Write a program to identify all prime numbers between 1 and 100 using list comprehensions.

prime_numbers = [i for i in range(2, 101) if all(i % j for j in range(2, int(i ** 0.5) + 1))]
print(prime_numbers)