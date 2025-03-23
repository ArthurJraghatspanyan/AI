# Write a program that takes two strings as input and concatenates them with a space in between.
# # Input: "Good" and "Morning"
# # Output: "Good Morning"

str1 = input("Enter your 1st string: ")
str2 = input("Enter your 2nd string: ")

print(str1 + chr(32) + str2)