# Write a function filter_positive that takes a list of numbers and returns a new list containing only the positive numbers.
# print(filter_positive([-5, 3, -1, 2, 0]))  # Example call

def filter_positive(ls):
  positives = []
  for i in ls:
    if i > 0:
      positives.append(i)
  return positives

print(filter_positive([-5, 3, -1, 2, 0]))