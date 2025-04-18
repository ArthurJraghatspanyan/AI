def custom_contain(it, st):
  for i in range(len(it)):
    if it[i] == st:
      return True
  return False

ls = "Hello "
st = " "
print(custom_contain(ls, st))