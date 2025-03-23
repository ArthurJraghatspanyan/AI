# Use a set to create a list of vocabulary words from a paragraph.
# Break the paragraph into individual words, add each word to the set, and print the final set of unique words.
# Example: For the paragraph "Python is fun. Python is powerful.", the output should be {"Python", "is", "fun", "powerful"}.

sentence = input("Enter your sentence: ")
st = set(sentence.strip().split())

print(st)