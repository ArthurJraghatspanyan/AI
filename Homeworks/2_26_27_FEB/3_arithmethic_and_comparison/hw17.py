# Compare the values of a float and an int and print whether they are equal or not.

num_int = int(input("Enter your integer number: "))
num_float = float(input("Enter your float number: "))

if num_int > num_float:
  print("Integer is greater than float")
elif num_int < num_float:
  print("Integer is less than float")
else:
  print("Equal")