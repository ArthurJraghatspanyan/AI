# Create a class named Car with no methods or attributes. Then, create an instance of this class and print the type of the instance.

class Car:
  pass

car = Car()
print(type(car))

print()

# Modify the Car class to accept brand and model as parameters during object creation. Then, create an instance and print the attributes.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

toyota = Car("Toyota", "Corolla")
print(toyota.brand)
print(toyota.model)

print()

# Extend the Car class by adding a method display_info() that prints the brand and model of the car.

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
  
  def display_info(self):
    print(self.brand)
    print(self.model)

bmw = Car("BMW", "M5")
bmw.display_info()

print()

# Modify the Car class to have a default value for the model ("Unknown"). If the model is not provided during initialization, it should use the default value.

class Car:
  def __init__(self, brand, model="X-Trail"):
    self.brand = brand
    self.model = model
  def display_info(self):
    print(self.brand)
    print(self.model)

nissan = Car("Nissan")
nissan.display_info()