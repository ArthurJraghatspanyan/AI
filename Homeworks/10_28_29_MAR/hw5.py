# Even Numbers Generator
# Objective
  # Practice filtering logic within a generator.
  # Reinforce the idea of yielding only certain values (in this case, even numbers).
# Task
  # Write a generator function even_numbers(nums) that takes a list (or any iterable) of integers and yields only those that are even.
  # Test it on a small list of mixed even/odd integers.
  # Print each yielded value to confirm it’s even.

import typing

def even_numbers(nums):
  if not isinstance(nums, typing.Iterable):
    raise TypeError("Type must be iterable.")
  return (num for num in nums if num % 2 == 0)

numbers_list = [1, 2, 3, 4, 5, 10, 11, 14]
for even in even_numbers(numbers_list):
  print(even)