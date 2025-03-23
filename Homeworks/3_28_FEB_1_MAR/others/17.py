# Write a program using a while loop that repeatedly asks the user to input a number until
# they input 0, then print the sum of all entered numbers.

sum = 0
num = 1 # To not exit loop

while num:
  num = int(input("Enter your number: "))
  sum += num
print(f"Summary of numbers: {sum}")