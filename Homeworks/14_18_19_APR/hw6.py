# Remove Blank Lines from a File
# File Name: data.txt
# Description: Write a program to remove all blank lines from data.txt and save the cleaned content to cleaned_data.txt.
# Initial File Content in data.txt:
# Line 1: Important data.

# Line 2: More data.


# Line 3: End of file.

fd1 = open('data.txt')
content1 = fd1.readlines()
fd2 = open('cleaned_data.txt', 'a')
for text in content1:
  if text == '\n':
    continue
  fd2.write(text)