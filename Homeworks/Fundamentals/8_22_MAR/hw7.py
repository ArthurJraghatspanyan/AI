# Reverse a String
# Write a recursive function to reverse a given string.
# Reversing a string means rearranging its characters from the last to the first.
# For example, the string "hello" becomes "olleh".

def reverse_string(s):
  if len(s) == 0:
    return ""
  return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello"))