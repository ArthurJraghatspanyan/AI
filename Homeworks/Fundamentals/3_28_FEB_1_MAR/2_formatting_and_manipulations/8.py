# Write a program to convert all characters in a string to uppercase and then to lowercase.

# Variation 1: Built in

st = input("Enter your string: ")

print(f"Built in.\nUpper: {st.upper()}\nLower: {st.lower()}")

# Variation 2: Manual

max = ""
min = ""

for i in st:
  if ord(i) in range(65, 91):
    max += i
    min += chr(ord(i) + 32)
  elif ord(i) in range(97, 123):
    min += i
    max += chr(ord(i) - 32)
  else:
    max += i
    min += i

print(f"Manual.\nUpper: {max}\nLower:{min}")