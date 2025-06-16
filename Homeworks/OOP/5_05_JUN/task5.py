# Task 5: Diamond Problem – Role Behavior

class Person:
  def role(self):
    pass

class Teacher(Person):
  def role(self):
    print("Teaching")

class Researcher(Person):
  def role(self):
    print("Researching")

class Professor(Teacher, Researcher):
  def role(self):
    super().role()

Professor().role()    # Teaching because super() searches first class after Professor in mro and takes it's method.