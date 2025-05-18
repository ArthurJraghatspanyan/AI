# Sum of Digits
# Write a recursive function to calculate the sum of all digits in a number.
# For example, the digits of 1234 add up to 1 + 2 + 3 + 4 = 10.

def sum_of_digits(n):
  if n == 0:
    return 0
  return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(567))