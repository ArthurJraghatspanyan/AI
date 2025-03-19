def binary(num):
  binar = ""
  while num != 0:
    if num % 2 == 0:
      binar = str(0) + binar
      num //= 2
    elif num % 2 == 1:
      binar = str(1) + binar
      num //= 2
  return int(binar)

res = binary(13)
print(res)