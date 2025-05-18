# Գրել ծրագիր, որը ստանում է ամբողջ թիվ։ Հայտարարել list: Եթե list-ում առկա է տրված թիվը տպել YES, հակառակ դեպքում տպել NO։

ls = [45, 32, 16, 3.16, 148, 149]
num = input("Enter your number: ")
if num.isdigit() or '.' in num:
  num = float(num)
  if num in ls:
    print("YES")
  else:
    print("NO")
else:
  print("Wrong type entered. Try again!")