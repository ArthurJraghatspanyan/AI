# Find the Maximum Element in a List
# Write a recursive function to find the maximum element in a list.
# For example, in the list [3, 1, 4, 1, 5], the maximum element is 5.

def find_max_element(ls):
  if not ls:
    return 0
  elif len(ls) == 1:
    return ls[0]
  max = ls[0]
  if max < find_max_element(ls[1:]):
    return max

print(find_max_element([3, 1, 4, 1, 5]))