# Flatten a Nested List
# Write a recursive function to flatten a list containing nested lists.
# For example, the list [1, [2, [3, [4]]], 5] should become [1, 2, 3, 4, 5].

def flatten_list(ls):
  result = []
  for i in ls:
    if isinstance(i, list):
      result.extend(flatten_list(i))
    else:
      result.append(i)
  return result

print(flatten_list([1, [2, [3, [4]]], 5]))