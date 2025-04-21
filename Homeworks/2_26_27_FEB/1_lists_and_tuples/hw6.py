# Write a program to access elements from a nested list and a nested tuple.

ls = [1, 2, 3, ["Hello", "World"]]
tp = (4, 5, 6, ("Spam", "Foo"))

# Variation 1: Indexing

print("Indexing:\n")
print(f"Elements in nested list: {ls[3][:]}")
print(f"Elements in nested tuple: {tp[3][:]}\n\n")

# Variation 2: Using loop

print("Using loop:\n")
print("Elements in nested list:\n")

for i in ls:
  if type(i) == list:
    print(i)
    for j in i:
      print(j)

print("\nElements in nested tuple:\n")

for k in tp:
  if type(k) == tuple:
    print(k)
    for m in k:
      print(m)