# Recursively extract the secondary diagonal elements’ sum  from a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def recursive_diagonal(matrix, i=0):
  if not matrix:
    return 0
  return matrix[0][len(matrix[0]) - 1 - i] + recursive_diagonal(matrix[1:], i + 1)

print(recursive_diagonal(matrix))