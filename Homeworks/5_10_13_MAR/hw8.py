# Write a program with a global variable x. Create a function that changes the value of x inside the function
# and prints both the global and local values.

# modify_variable()
# print("Global x:", x)

x = 10
def modify_variable():
  global x;
  x = "Hello"

modify_variable()
print("Global x:", x)