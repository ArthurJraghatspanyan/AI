# Write a function display_student_info that accepts any number of keyword arguments and prints them in the format: key: value.
# Call the function with keyword arguments such as name="Alice", age=20, and major="CS".
# Experiment with passing different sets of keyword arguments.

def display_student_info(**kwargs):
  di = {}
  for key, value in kwargs.items():
    di[key] = value
  return di

print(display_student_info(name="Alice", age=20, major="CS"))
print(display_student_info(name=("Bob", "Joe"), age=22, major="CS"))
print(display_student_info(name="Tom", age=21, course=3, major="CS"))
print(display_student_info(name="Angela", age=18, course=1, faculty="Physics"))