# Write a program to filter and print words from a list of strings that start with vowels using list comprehension.

ls = ["Apple", "banana", "Orange", "guitar", "Umbrella", "elephant", "Mountain", "tiger"]
vowels = "aeiouAEIOU"

res = [i for i in ls if i[0] in vowels]
print(res)