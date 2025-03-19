def even_in_sequence():
  even = []
  for i in range(2, 201, 2):
    even.append(i)
  return even

res = even_in_sequence()
print(res)