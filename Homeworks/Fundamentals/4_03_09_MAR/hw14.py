# 2. Word Frequency Analyzer (Dictionaries)
# Given a paragraph of text, count how many times each word appears and find the most common words.

paragraph = """Nory was a Catholic because her mother was a Catholic, and Nory’s mother was a Catholic because her father was a Catholic, and her father was a Catholic because his mother was a Catholic, or had been."""

words = []
word = ""

for i in paragraph:
  if ord(i) in range(65, 91) or ord(i) in range(97, 123):
    word += i
  else:
    words.append(word)
    word = ""

di = {}

for item in words:
  if item not in di:
    di[item] = 1
  else:
    di[item] += 1

print(di)