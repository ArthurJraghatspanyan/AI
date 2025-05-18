# Determine Absolute Path of a File
  # File Name: config/settings.txt
  # Description: Write a program to determine and print the absolute path of the file settings.json,
  # which is located in the config folder relative to the script directory.
  # Absolute path: /home/user/project/config/settings.json

import os

print(os.path.abspath('config/settings.txt'))