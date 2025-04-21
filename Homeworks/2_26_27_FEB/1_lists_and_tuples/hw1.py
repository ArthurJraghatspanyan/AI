# Write a program that prompts the user to create an empty list. Then, the user should be able to add elements to the list using three different methods: append(), extend(), and insert().
# Use append() to add a single element to the end of the list.
# Use extend() to add multiple elements (from another list or iterable) at the end of the list.
# Use insert() to add an element at a specific index in the list.

ls = []

ls.append(12)
ls.extend([123, "Hello"])
ls.insert(1, ("World", "Bye"))

print(ls)


# Extend the previous program to allow the user to remove elements using two methods: remove() and pop().
# Use remove() to remove a specific element by its value.
# Use pop() to remove an element at a specific index.

ls.remove(12)
ls.pop(0)

print(ls)