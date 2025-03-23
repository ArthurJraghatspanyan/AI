# Իրականացնել ռեկուրսիվ ֆունկցիա, որը կստանա տող և կվերադարձնի տողի երկարությունը։

def len_of_str(st):
  if not st:
    return 0
  return 1 + len_of_str(st[1:])

print(len_of_str("Hello"))