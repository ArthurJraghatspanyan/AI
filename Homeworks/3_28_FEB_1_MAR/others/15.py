# Count how many vowels are in the string and print the count.

st = input("Enter your string: ")
vowels = "aeiouAEIOU"
vowels_count = 0
for i in st:
  if i in vowels:
    vowels_count += 1

print(vowels_count)