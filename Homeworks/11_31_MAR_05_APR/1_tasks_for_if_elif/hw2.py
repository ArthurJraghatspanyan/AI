# Using a list comprehension, create a new list from [1, 2, 3, -4, -5, 6] that contains only the positive numbers.

ls = [1, 2, 3, -4, -5, 6]
ls = [i for i in ls if i > 0]
print(ls)