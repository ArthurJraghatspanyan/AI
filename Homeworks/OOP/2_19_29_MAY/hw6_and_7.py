# Task 6: Basic Encapsulation with Getters and Setters

class Person:
  def __init__(self, name: str = "James"):
    self.__name = name
  def get_name(self):
    return self.__name
  def set_name(self, newName: str):
    if not isinstance(newName, str):
      raise TypeError("Name type must be string")
    if not newName:
      raise ValueError("String must not be empty.")
    self.__name = newName

person = Person()
print(person.get_name())
person.set_name("Bob")
print(person.get_name())

print()

# Task 7: Using Python’s @property Decorators

# Refactor the Person class from Task 1 to:
  # Use the @property decorator for the getter.
  # Use the @name.setter decorator for the setter.

class Person:
  def __init__(self, name: str = "James"):
    self.__name = name
  @property
  def name(self):
    return self.__name
  @name.setter
  def name(self, newName: str):
    if not isinstance(newName, str):
      raise TypeError("Name type must be string")
    if len(newName) < 3:
      raise ValueError("Name length must have at least 3 characters.")
    self.__name = newName

person1 = Person()
print(person1.name)
person1.name = "Tom"
print(person1.name)