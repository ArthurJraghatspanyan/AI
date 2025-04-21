# Create a program that extracts the first 5 characters from a given string.

string = "Hello, World"

# Variation 1: Slicing

print(f"Slicing: {string[:5]}")

# Variation 2: Manual

first_5 = ""

for i in range(len(string)):
  if i == 5:
    break
  first_5 += string[i]

print(f"Manual: {first_5}")