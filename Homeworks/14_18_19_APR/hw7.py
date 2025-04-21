# Binary File Copy
  # Source File: image.jpg
  # Destination File: copy_image.jpg
  # Description: Write a program to copy the content of a binary file image.jpg into a new file copy_image.jpg.
  # Ensure that the copied file is identical to the original.

fd1 = open('image.jpg', 'rb')
content = fd1.read()
fd2 = open('copy_image.jpg', 'wb')
fd2.write(content)