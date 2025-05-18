# User Input for File Name
  # Description: Write a program that prompts the user to input a file name. Create a new file with that name using
  # x mode and write "File <filename> created successfully." into it. If the file already exists, notify the user.
  # Catch FileExistsError and notify the user if the file exists.

filename = input("Enter a file name: ")
if not filename.endswith('.txt'):
  raise ValueError("Format must end with '.txt'.")

try:
  fd = open(filename, 'x')
  fd.write(f"File {filename} created successfully.")
except:
  raise FileExistsError("File already exists.")