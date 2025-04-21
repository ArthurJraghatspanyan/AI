# Generator Expression for Data Transformation

# Objective
  # Introduce generator expressions (parentheses syntax).
  # Compare and contrast list comprehensions vs. generator expressions.
# Task
  # Create a list of integers: numbers = list(range(1, 11)).
  # Use a list comprehension to create squares_list (the square of each number).
  # Use a generator expression to create squares_gen.
  # Print both squares_list and then iterate over squares_gen. Observe how squares_gen does not store all items in memory at once.

numbers = list(range(1, 11))

squares_list = [num ** 2 for num in numbers]
squares_gen = (num ** 2 for num in numbers)

print(squares_list)
for num in squares_gen:
  print(num)