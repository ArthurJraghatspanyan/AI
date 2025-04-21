# Generate a Summary Report
# File Name: log.txt
  # Description: Write a program to analyze a log file log.txt and generate a report of the total number of occurrences
  # for each log level (INFO, WARNING, ERROR) in a new file summary.txt.
  # Example Content in log.txt:
  # INFO: Application started.
  # WARNING: Low memory.
  # ERROR: Failed to load module.
  # INFO: User logged in.
  # ERROR: Unable to save file.

  # INFO: 2
  # WARNING: 1
  # ERROR: 2

target = ("INFO", "WARNING", "ERROR")
fd1 = open('log.txt')
content = fd1.read()
fd2 = open('summary.txt', 'w')
for i in target:
  fd2.write(i + ":" + str(content.count(i)) + "\n")