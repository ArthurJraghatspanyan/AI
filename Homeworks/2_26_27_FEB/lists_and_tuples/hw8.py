# Write a program to reverse a list and a tuple.

ls1 = [1, 2, 3]
tp1 = (4, 5, 6)

# Variation 1: Using built-ins

ls1.reverse()
tp_reversed = tuple(reversed(tp1))

print("Built-in:\n")
print(f"Reversed list: {ls1}, Reversed tuple: {tp_reversed}\n")

# Variation 2: Manual

ls2 = [1, 2, 3]
tp2 = (4, 5, 6)

reversed_list = []
reversed_tuple = ()
for i in range(len(ls2) - 1, -1, -1):
  reversed_list.append(ls2[i])

for j in range(len(tp2) - 1, -1, -1):
  to_list = list(reversed_tuple)
  to_list.append(tp2[j])
  reversed_tuple = tuple(to_list)

print("Manual:\n")
print(f"Reversed list: {reversed_list}, Reversed tuple: {reversed_tuple}")