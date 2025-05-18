# Write a program that takes a sentence and splits it into words, then joins the words back into a sentence with hyphens (-) between them.
# # Input: "I love Python"
# # Output: "I-love-Python"

string = input("Enter your string: ")
ls = string.split(sep=' ')
result = "-".join(ls)

print("Output:", result, '\n')