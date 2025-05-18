# Write a program to find and print the maximum and minimum values in a list and a tuple.

ls = [10, 52, -24, -3, 25, 7]
tp = (92, -142, 85, -61, 423, 139)

# Variation 1: Using built-ins
print("Built-in:\n")
print(f"Maximum value of list: {max(ls)}, Minimum: {min(ls)}")
print(f"Maximum value of tuple: {max(tp)}, Minimum: {min(tp)}\n")

# Variation 2: Manual

max_ls = ls[0]
min_ls = ls[0]
max_tp = tp[0]
min_tp = tp[0]

for i in range(1, len(ls)): # To not compare 1st element with first
  if ls[i] > max_ls:
    max_ls = ls[i]
  if ls[i] < min_ls:
    min_ls = ls[i]

for j in range(1, len(tp)):
  if tp[j] > max_tp:
    max_tp = tp[j]
  if tp[j] < min_tp:
    min_tp = tp[j]

print("Manual:\n")
print(f"Maximum value of list: {max_ls}, Minimum: {min_ls}")
print(f"Maximum value of tuple: {max_tp}, Minimum: {min_tp}")