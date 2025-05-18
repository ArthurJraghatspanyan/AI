# Write a function power that takes a number and an optional exponent. The default exponent should be 2 (square the number).
# print(power(3)) # 3^2 
# print(power(3, 3)) # 3^3

def power(num, exp = 2):
  return num ** exp

print(power(3))
print(power(3, 3))