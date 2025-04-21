# Write to a File
  # File Name: output.txt
  # Description: Create a file named output.txt and write the text "Python is fun!" into it.
  # Close the file and reopen it to verify its content.

fd = open('output.txt', mode='w')
fd.write("Python is fun!")