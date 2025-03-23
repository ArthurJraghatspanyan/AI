# Create a dictionary to store student names as keys and their scores as values.
# Use a few sample names and scores to populate the dictionary.
# Print out each student’s name and score on a new line.

di = {
  "Arthur": 96,
  "Joe": 97,
  "Ann": 98
}

for key, value in di.items():
  print(key, ":", value)