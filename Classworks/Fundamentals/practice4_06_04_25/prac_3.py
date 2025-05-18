# Write a generator function transpose_rows(matrix) that takes a 2D matrix (list of lists) and yields its transposed version.

import typing

def transpose_row(matrix):
  if not isinstance(matrix, typing.Iterable):
    raise TypeError("Object must be iterable")
  for i in range(len(matrix[0])):
    if not isinstance(matrix[i], typing.Iterable):
      raise TypeError("Object must be iterable")
    tmp = []
    for j in range(len(matrix)):
      tmp.append(matrix[j][i])
    yield tmp

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list(transpose_row(matrix)))