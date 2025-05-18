# Append to a File
  # File Name: notes.txt
  # Description: Open the file notes.txt in append mode and add the text "Remember to review file handling in Python!"
  # as a new line at the end. If the file does not exist, create it.

fd = open('notes.txt', mode='a')
fd.write("\nHello World")