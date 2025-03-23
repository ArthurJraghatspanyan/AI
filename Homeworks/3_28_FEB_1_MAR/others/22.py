# Հայտարարել list,  որը բաղկացած է string-ներից: Տպել թե քանի անգամ է յուրաքանչյուրը հանդիպում list-ում:

ls = ["Hello", "World", "Python", "Hello", "Python", "Hello"]
ls2 = []

for i in ls:
  if i not in ls2:
    ls2.append(i)

for j in ls2:
  count = 0
  for i in ls:
    if j == i:
      count += 1
  print(f"{j}: {count}")