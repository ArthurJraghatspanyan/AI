# Extract the diagonal elements from a matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

res = []

for i in range(len(matrix)):
  res.append(matrix[i][i])

print(res)