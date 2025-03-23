# Write a function sum_up_to_n(n) that returns the sum of numbers from 1 to n using recursion.

def sum_up_to_n(n):
  summary = 0
  if n <= 1:
    return 1
  summary += n + sum_up_to_n(n - 1)
  return summary

print(sum_up_to_n(6))