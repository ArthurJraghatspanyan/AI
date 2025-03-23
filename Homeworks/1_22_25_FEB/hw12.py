# Write a program that counts how many times the letter "a" appears in a given string.
# # Input: "banana"
# # Output: "a" appears 3 times

string = input("Enter your string: ")
target = 'a'

# 1st variation: built-in function

print(f"\nOutput with built-ins: 'a' appears {string.count(target)} times\n")

# 2nd variation: manually

target_count = 0

for i in string:
  if i == target:
    target_count += 1

print(f"Output with manually: 'a' appears {target_count} times")