# Create a program to count the number of occurrences of a specific character in a string.

string = "Hello World"
spec_char = 'l'
char_count = 0

for i in string:
  if i == spec_char:
    char_count += 1

print(f"Count of {spec_char} in {string}: {char_count}")