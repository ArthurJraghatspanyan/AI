# Create a class Student that keeps track of the total number of students created using a class variable.

class Student:
  num_of_students = 0
  def __init__(self):
    Student.num_of_students += 1

student1 = Student()
student2 = Student()
student3 = Student()

print(f"Total students: {student3.num_of_students}")

# Modify the Student class to include a __str__ method so that printing a student instance displays their name.

class Student:
  num_of_students = 0
  def __init__(self, name):
    self.name = name
    Student.num_of_students += 1
  
  def __str__(self):
    return f"Name of student is: {self.name}"

student1 = Student("Ann")
print(student1)