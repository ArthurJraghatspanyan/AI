# Write a function reverse_string(s) that reverses a string without using slicing or built-in functions like reversed().
# Use a loop to construct the reversed string.

def reverse_string(s):
  reversed_st = ""
  for i in s:
    reversed_st = i + reversed_st
  return reversed_st

print(reverse_string("HelloWorld"))