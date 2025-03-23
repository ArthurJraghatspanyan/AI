# Binary Search
# Write a recursive binary search algorithm to find the index of a target value in a sorted array.
# Binary search divides the array into halves to find the target more efficiently.

def binary_search(arr, target, left, right):
  if left > right:
    return -1
  mid = (left + right) // 2
  if arr[mid] == target:
    return mid
  elif arr[mid] >= target:
    return binary_search(arr, target, left, mid - 1)
  else:
    return binary_search(arr, target, mid + 1, right)

ls = [2, 4, 6, 8]
print(binary_search(ls, 5, 0, len(ls) - 1))