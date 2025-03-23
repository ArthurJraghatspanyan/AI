# Write a program to print every second character from a string.

str = "Welcome To Python"

# Variation 1: Slicing

print(f"Slicing: {str[1::2]}")

# Variation 2: Manual

every_second = ""

for i in range(1, len(str), 2):
  every_second += str[i]

print(f"Manual: {every_second}")