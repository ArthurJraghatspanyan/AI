# Create a File Using a Relative Path
  # Description: Create a new text file named relative_output.txt in a folder called relative_files
  # (located relative to your script's directory). Write "This is a file created using a relative path." into the file.
  # Check if the relative_files directory exists. If not, create it.

import os

relative_path = 'relative_files'
if not os.path.exists(relative_path):
  os.mkdir(relative_path)
else:
  print("Relative directory already exists")
fd = open('relative_files/relative_output.txt', 'w')
fd.write("This is a file created using a relative path.")