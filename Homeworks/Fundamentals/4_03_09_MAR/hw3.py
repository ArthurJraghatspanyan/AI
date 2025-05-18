# Create a dictionary that maps numbers from 1 to 5 to their word equivalents (e.g., {1: "one", 2: "two", ...}).
# Use this dictionary to convert a list of numbers into words and print each word on a new line.

ls = ["one", "two", "three", "four", "five"]
di = {}

for i in range(len(ls)):
  if ls[i] not in di:
    di[i + 1] = ls[i]

for value in di.values():
  print(value)