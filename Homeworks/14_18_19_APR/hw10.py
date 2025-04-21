# Read a File Using a Relative Path
  # File Name: data_files/example_data.txt
  # Description: Open the file example_data.txt located in the data_files folder (relative to the script directory).
  # Print its content to the console.
  # Ensure that the folder data_files exists and contains the file example_data.txt.

import os

if not os.path.exists('data_files/example_data.txt'):
  raise FileNotFoundError("Path doesn't exist. Create it.")
fd = open('data_files/example_data.txt')
print(fd.read())