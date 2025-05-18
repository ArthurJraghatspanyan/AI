# Create a class Person with attributes name and age. Create three instances of this class and store them in a list.
# Then, loop through the list and print each person's information.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display_info(self):
    return f"\nName: {self.name}\nAge: {self.age}"

ls = []
person1 = Person("James", 20)
ls.append(person1)
person2 = Person("Bob", 21)
ls.append(person2)
person3 = Person("Ann", 22)
ls.append(person3)

for instance in ls:
  print(instance.display_info())