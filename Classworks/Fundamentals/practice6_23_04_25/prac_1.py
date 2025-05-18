# Create a generator function generate_orders() that yields 50 simulated orders:
# Each order is a dictionary with fields like:
# {
#     "order_id": "ORD123",
#     "customer": "John Doe",
#     "amount": 120.50,
#     "status": "pending"
# }

import random

valid = []
order_id = 20
customers = ("Emma Johnson", "Liam Carter", "Olivia Brooks", "Noah Bennett", "Ava Mitchell", "Ethan Reynolds", "Sophia Hughes", "Mason Perry", "Isabella Price", "Logan Simmons")
statuses = ("pending", "processing", "shipped", "cancelled")
invalid = open('invalid_orders.txt', 'w')

def validate_orders(fn):
  def inner(*args, **kwargs):
    global statuses
    global valid
    res = fn(*args, **kwargs)
    invalid = open('invalid_orders.txt', 'a')
    for order in res:
      if order["amount"] > 0 and order["status"] in statuses:
        valid.append(order)
      else:
        invalid.write(str(order) + "\n")
    return res
  return inner

@validate_orders
def generate_orders():
  di = {}
  global order_id
  global customers
  global statuses
  amount = random.uniform(-1000, 1000)
  di["order_id"] = order_id
  di["customer"] = random.choice(customers)
  di["amount"] = float(f"{amount:.2f}")
  di["status"] = random.choice(statuses)
  yield di
  order_id += 1

for _ in range(50):
  generate_orders()

for i in valid:
  print(i)

valid.clear()