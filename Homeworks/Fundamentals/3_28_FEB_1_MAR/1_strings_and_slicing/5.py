# Replace all occurrences of a specific character with another character in a string.

string = "Hello World. Welcome to Python. This is homework."

# Variation 1: Using built-ins

print(f"Built-in: {string.replace('.', '!')}")

updated_str = ""

for i in string:
  if i == '.':
    updated_str += '!'
    continue
  updated_str += i

print(f"Manual: {updated_str}")