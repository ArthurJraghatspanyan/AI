# Copy File Content
  # Source File: source.txt
  # Description: Write a program to copy the content of source.txt into destination.txt.
  # If the destination file already exists, overwrite its content.
  # Example Content in source.txt: File handling in Python is powerful and efficient.

fd1 = open('source.txt')
content = fd1.read()
fd2 = open('destination.txt', 'w')
fd2.write(content)