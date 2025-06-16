# Task 2 – Advanced MRO and Multiple Inheritance

class Animal:
  def make_sound(self):
    pass

class Mammal(Animal):
  def make_sound(self):
    print("Generic mammal sound")

class Pet(Animal):
  def make_sound(self):
    print("Generic pet sound")

class Dog(Mammal, Pet):
  def make_sound(self):
    print("Bark!")

