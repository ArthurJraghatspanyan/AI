# Palindrome Check
# Write a recursive function to check if a string is a palindrome.
# A palindrome is a string that reads the same backward as forward. For example, "madam" is a palindrome, but "hello" is not.

def is_palindrome(s):
  if len(s) <= 1:
    return True
  if s[0] != s[-1]:
    return False
  return is_palindrome(s[1:-1])

print(is_palindrome("radar"))