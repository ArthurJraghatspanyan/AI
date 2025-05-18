# Create a class Employee with name and salary. Add a method give_raise(amount) that increases the salary

class Employee:
  def __init__(self, name: str, salary: int):
    if not isinstance(name, str) or not isinstance(salary, (int, float)):
      raise TypeError("Wrong types for name: str and/or salary: int | float")
    if salary < 100000:
      raise ValueError("Employee is not Indian! Set a normal salary for him!")
    self.name = name
    self.salary = salary
  
  def give_raise(self, amount):
    if not isinstance(amount, (int, float)):
      raise TypeError("Amount must be integer of float type!")
    if amount <= 0:
      raise ValueError("Amount must be greater than 0!")
    
    self.salary += amount

employee1 = Employee("Sean", 100000)
print(employee1.salary)
employee1.give_raise(50000)
print(employee1.salary)