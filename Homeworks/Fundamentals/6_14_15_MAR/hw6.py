# Իրականացնել int տիպի արժեք վերադարձնող ֆունկցիա, որը վերադարձնում է՝ 1, եթե ֆունկցային փոխանցված ամբողջ թիվը
# կարող է արտահայտվել երկու պարզ թվերի գումարով, հակառակ դեպքում ֆունկցիան կվերադարձնի՝ 0:

def is_prime(n):
  for i in range(2, n // 2 + 1):
    if n % i == 0:
      return False
  return True

def is_sum_of_two_primes(num):
  if num <= 3:
    return 0
  for i in range(2, num // 2 + 1):
    if is_prime(i):
      if is_prime(num - i):
        return 1
  return 0

print(is_sum_of_two_primes(56))