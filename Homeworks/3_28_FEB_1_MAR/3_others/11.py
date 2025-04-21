# Create a program to find the sum of the first and last digit of a given number.

num = 7236
sum = 0
num_str = str(abs(num))
for i in range(len(num_str)):
  if i == 0:
    sum += int(num_str[i])
  sum += int(num_str[len(num_str) - 1])
  break

print(sum)