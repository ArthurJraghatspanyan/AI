# Write a function print_characters(s) that prints each character of a string sss on a new line using recursion.

def print_characters(s):
  start = s[0]
  if start == s[-1]:
    return s[-1]
  print(start)
  return print_characters(s[1:])

print(print_characters("HelloWorld"))