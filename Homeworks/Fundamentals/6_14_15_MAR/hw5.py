# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը:

def sum_of_digits(num):
  summary = 0
  while num != 0:
    summary += num % 10
    num //= 10
  return summary

print(sum_of_digits(455))