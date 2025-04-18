ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

sum = 0
for i in range(len(ls)):
  sum += ls[i][i]

print(sum)