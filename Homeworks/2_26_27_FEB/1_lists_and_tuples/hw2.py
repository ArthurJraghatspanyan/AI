# Write a program that prompts the user to create a list containing different types of elements (integers, strings, floating-point numbers, etc.). Allow the user to add elements of different types to the list using append(), extend(), and insert().
# The user should be able to add elements of different types (e.g., int, float, str) to the list.
# Demonstrate adding elements using all three methods.

ls = [12, "Hello", 3.14, True, (1, 2, 3), [4, 5, 6], {"Key": "Value"}]
ls.append("World")
ls.extend({7, 8, 9})
ls.insert(2, "Welcome")

print(ls)