# Write a program that categorizes numbers in a list as "Even", "Odd", or "Prime" using if-elif inside a loop.

import typing

def categorize(iterable, category):
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Type must be iterable.")
  if category == "Even":
    return [i for i in iterable if i % 2 == 0]
  elif category == "Odd":
    return [i for i in iterable if i % 2 != 0]
  elif category == "Prime":
    return [i for i in range(2, 101) if all(i % j for j in range(2, int(i ** 0.5) + 1))]
  else:
    raise ValueError("This type of category doesn't exist.")

ls = [i for i in range(101)]
print(categorize(ls, "Prime"))