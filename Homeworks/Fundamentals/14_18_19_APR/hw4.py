# Count Words in a File
  # File Name: story.txt
  # Description: Write a program to open the file story.txt, read its content, and
  # count the total number of words in the file. Display the count to the user.
  # Example Content: Once upon a time in a land far, far away, there lived a Python programmer.
  # Expected Output: Total words: 14

fd = open('story.txt')
res = fd.read()
ls = res.split()
count = 0
for i in ls:
  count += 1

print(f"Count of the words is: {count}")