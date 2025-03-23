# Իրականացնել ֆունկցիա, որն ընդունում է թիվ և վերադարձնում նրա թվանշանների գումարը:

def sum_of_digits(num):
  summary = 0
  for i in str(num):
    summary += int(i)
  return summary

print(sum_of_digits(45))