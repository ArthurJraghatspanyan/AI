# Implement a function reverse_string that accepts a string and returns it reversed without using built-in methods.

def reverse_string(st):
  if not isinstance(st, str):
    raise TypeError("Type must be string.")
  if not st:
    return st
  reversed_st = ""
  for char in st:
    reversed_st = char + reversed_st
  return reversed_st

print(reverse_string("213"))