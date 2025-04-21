# Accept two integer inputs from the user.
# Check if the first number is a multiple of the second and print True if it is, otherwise print False.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num2 % num1 == 0:
  print(True)
else:
  print(False)