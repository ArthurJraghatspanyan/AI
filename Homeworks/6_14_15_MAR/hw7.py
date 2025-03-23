# Իրականացնել ֆունկցիա, որը ունի հետևյալ նախատիպը (prototype)  def power (num: int, exp:int):
# Ֆունկցիան վերադարձնում է num ամբողջ թվի exp աստիճանի արժեքը։

def power(num, exp):
  if not isinstance(num, int) and not isinstance(exp, int):
    return "Error: Both - number and exponent must be integers!"
  if num == 0:
    return 0
  res = 1
  while exp > 0:
    if exp % 2 != 0:
      res *= num
    num *= num
    exp //= 2
  return res

print(power(5, 5))