# Simple Number Sequence Generator

def num_sequence(start, end):
  if not isinstance(start, int) and not isinstance(end, int):
    raise TypeError("Must be integer")
  if start >= end:
    raise ValueError("Starting value must be less than ending")
  for i in range(start, end + 1):
    yield i

res = num_sequence(1, 5)

for i in res:
  print(i)

print(list(res))