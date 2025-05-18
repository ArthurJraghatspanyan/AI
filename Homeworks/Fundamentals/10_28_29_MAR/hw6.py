# Cumulative Sum Generator
# Objective
  # Create a generator that computes and yields partial sums.
  # Illustrate maintaining state (running total) within a generator.
# Task
  # Write a generator function cumulative_sum(nums) that takes a list (or any iterable) of numbers.
  # As you iterate through each number, keep adding it to a running total and yield the new total each time.
  # Test it on a small list, printing each partial sum.

import typing

def cumulative_sum(nums):
  if not isinstance(nums, typing.Iterable):
    raise TypeError("Type must be iterable.")
  summary = 0
  for i in nums:
    summary += i
    yield summary

numbers_list = [1, 3, 5, 2]
for partial_sum in cumulative_sum(numbers_list):
  print(partial_sum)