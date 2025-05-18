# Read a File and Print its Content
  # File Name: example.txt
  # Description: The file example.txt contains several lines of text. Write a program to open the file in read mode and
  # print each line, stripping any leading or trailing whitespace.

fd = open('example.txt')
print(fd.read())