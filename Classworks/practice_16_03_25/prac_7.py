def square_of_number(num):
  if num == 0:
    return False
  num = abs(num)
  it = 1
  while it * it <= num:
    it += 1
  
  return it - 1


print(square_of_number(4))