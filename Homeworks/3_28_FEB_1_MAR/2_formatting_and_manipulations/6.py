# Write a program to print a formatted message like: "Hello, my name is James and I am 20 years old." using f-strings.

# Variation 1
name = 'James'

print("Hello, my name is %s and I am %d years old." %(name, 20))

# Variation 2

print("Hello, my name is {0} and I am {1} years old.".format("James", 20))

# Variation 3

name = "James"
age = 20

print(f"Hello, my name is {name} and I am {age} years old.")