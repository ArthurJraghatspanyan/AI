# Write a program to find the sum of all elements in a list and a tuple.

ls = [1, 2, 3]
tp = [4, 5, 6]

# Variation 1: Using built-ins

print("Built-in:\n")
print(f"Summary of list: {sum(ls)}, And of tuple: {sum(tp)}")
print()

# Variation 2: Manually

summary_ls = 0
summary_tp = 0

for i in ls:
  summary_ls += i
for j in tp:
  summary_tp += j

print("Manual:\n")
print(f"Summary of list: {summary_ls}, And of tuple: {summary_tp}")