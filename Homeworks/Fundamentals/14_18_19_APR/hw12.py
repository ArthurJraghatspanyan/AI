# Create a New File
  # File Name: exclusive_file.txt
  # Description: Write a program to create a new file named exclusive_file.txt using the x mode and write the text
  # "This file is created using x mode." into it. Ensure the program handles errors gracefully if the file already exists.
  # Use a try...except block to catch the FileExistsError if the file already exists.

try:
  fd = open("exclusive_file.txt", 'x')
  fd.write("This file is created using x mode.")
except:
  raise FileExistsError("File already exists")