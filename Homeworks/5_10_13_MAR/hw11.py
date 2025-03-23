# Write a function calculate_discount that takes a price and a discount percentage and returns the discounted price.
# print(calculate_discount(100, 20))  # 20% off on 100

def calculate_discount(price, discount):
  res = price * discount // 100
  return f"{res}% off on 100"

print(calculate_discount(100, 25))