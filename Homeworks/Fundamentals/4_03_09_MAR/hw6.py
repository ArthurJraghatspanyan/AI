# Given a list of numbers, use a set to find any duplicates in the list and print them.
# You can add numbers to a set one by one and check if they are already present.
# Example: For the list [1, 2, 2, 3, 4, 4, 5], the output should be {2, 4}.

ls = [1, 2, 2, 3, 4, 4, 5]
st1 = set()
st2 = set()

for i in ls:
  if i not in st1:
    st1.add(i)
  else:
    st2.add(i)

print(st2)