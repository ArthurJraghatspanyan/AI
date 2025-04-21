# Write a program to find the maximum of three numbers using nested conditional operators.

ls = [125, 123, 126]

if ls[0] > ls[1]:
  if ls[0] > ls[2]:
    print(f"{ls[0]} is maximum")

if ls[1] > ls[0]:
  if ls[1] > ls[2]:
    print(f"{ls[1]} is maximum")

if ls[2] > ls[0]:
  if ls[2] > ls[1]:
    print(f"{ls[2]} is maximum")