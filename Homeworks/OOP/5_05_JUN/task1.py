# Task 1 – Basic Polymorphism

class Animal:
  def make_sound(self):
    pass

class Dog(Animal):
  def make_sound(self):
    print("Bark!")

class Cat(Animal):
  def make_sound(self):
    print("Meow!")

class Cow(Animal):
  def make_sound(self):
    print("Moo!")

ls = [Dog(), Cat(), Cow()]

for i in ls:
  i.make_sound()