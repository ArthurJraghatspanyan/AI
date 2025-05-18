# Write a program that takes a string and converts it to both uppercase and lowercase.
# # Input: "Hello World"
# # Output: "HELLO WORLD" and "hello world"

string = input("Enter your string: ")

# 1st Variation: using built-in functions

print(f"\nOutput with bult-ins: {string.upper()} and {string.lower()}\n")

# 2nd Variation: doing it manually

str_upper = ""
str_lower = ""

for i in string:
  if ord(i) in range(65, 91):
    str_upper += i
    str_lower += chr(ord(i) + 32)
  elif ord(i) in range(97, 123):
    str_upper += chr(ord(i) - 32)
    str_lower += i

print(f"Output with manual: {str_upper} and {str_lower}\n")