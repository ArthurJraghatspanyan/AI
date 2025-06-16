# Task 1: Memory Optimization

import sys
import tracemalloc


class Person:
  __slots__ = ["name", "age"]

  def __init__(self, name, age):
    self.name = name
    self.age = age

class PersonWithoutSlots:
  def __init__(self, name, age):
    self.name = name
    self.age = age

def calculate_memory_usage_of_person():
  tracemalloc.start()

  for _ in range(1000000):
    Person("James", "15")

  current, peak = tracemalloc.get_traced_memory()

  return f"With __slots__:\nCurrent memory usage of Person: {current}\nPeak memory usage: {peak}"

def calculate_memory_usage_of_person_without_slots():
  tracemalloc.start()

  for _ in range(1000000):
    PersonWithoutSlots("James", 15)

  current, peak = tracemalloc.get_traced_memory()
  return f"Without __slots__:\nCurrent memory usage of Person: {current}\nPeak memory usage: {peak}"

size1 = sys.getsizeof(Person)
size2 = sys.getsizeof(PersonWithoutSlots)

print(f"Person size: {size1}\nPersonWithoutSlots size: {size2}")
print()
print(calculate_memory_usage_of_person())
print()
print(calculate_memory_usage_of_person_without_slots())