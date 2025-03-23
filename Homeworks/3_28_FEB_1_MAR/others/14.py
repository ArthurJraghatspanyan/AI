# Ask the user to enter a string, and then print the string in reverse order.

st = input("Enter your string: ")

# Variation 1: Concat

reversed_st = ""
for i in st:
  reversed_st = i + reversed_st

print("Concat.")
print(f"String: {st}\nReversed string: {reversed_st}\n")

# Variation 2: Range

reversed_st = ""
for i in range(len(st) - 1, -1, -1):
  reversed_st += st[i]

print("Range.")
print(f"String: {st}\nReversed string: {reversed_st}")