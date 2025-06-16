# Task 3: Simple Polymorphism – Vehicle Simulation

class Vehicle:
  def move(self):
    pass

class Car(Vehicle):
  def move(self):
    print("Car is moving on the road.")

class Bike(Vehicle):
  def move(self):
    print("Bike is moving on the track.")

class Airplane(Vehicle):
  def move(self):
    print("Airplane is flying in the sky.")

car = Car()
car.move()
bike = Bike()
bike.move()
airplane = Airplane()
airplane.move()