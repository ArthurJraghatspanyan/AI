# Write a program that takes a sentence and uses a set to find all unique words. Print each unique word on a new line.

sentence = input("Enter your sentence: ")
st = set(sentence.strip().split())

for i in st:
  print(i)