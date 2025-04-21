# Flatten a Nested List
# Write a recursive function to flatten a list containing nested lists.
# For example, the list [1, [2, [3, [4]]], 5] should become [1, 2, 3, 4, 5].

def flatten_list(ls):
  if len(ls) == 0:
    return []
  if isinstance(ls[0], list):
    return flatten_list(ls[0]) + flatten_list(ls[1:])
  return ls[:1] + flatten_list(ls[1:])

print(flatten_list([1, [2, [3, [4]]], 5]))