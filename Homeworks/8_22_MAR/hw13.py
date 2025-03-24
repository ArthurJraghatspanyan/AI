# Find the Maximum Element in a List
# Write a recursive function to find the maximum element in a list.
# For example, in the list [3, 1, 4, 1, 5], the maximum element is 5.

def find_max_element(ls):
  if not ls:
    return -1
  elif len(ls) == 1:
    return ls[0]
  max = find_max_element(ls[1:])
  if max > ls[0]:
    return max
  return ls[0]

print(find_max_element([3, 1, 4, 1, 5]))