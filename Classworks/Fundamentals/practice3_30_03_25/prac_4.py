# Իրականացնլ ռեկուրսիվ ֆունկցիա, որը ստանում է տող և վերադարձնում տողում առաջին հանդիպած մեծատառը։

def reverse_rec(st: str):
  if len(st) <= 1:
    if st.isupper():
      return st
    else:
      return -1
  char = st[0]
  if ord(char) in range(65, 91):
    return st[0]
  return reverse_rec(st[1::])

res = reverse_rec("helloWorld")
print(res)