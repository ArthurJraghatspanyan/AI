# Analyze the following code, explain why it raises an error, and fix the function call:

def book_ticket(destination, price, discount=0, *extras, **details):
  # print(f"Booking to {destination} for ${price - discount}")  # Mathematical error: Discount is not done correct
  print(f"Booking to {destination} for ${price - (price * discount // 100)}")  # The correct one
  if extras:
    print(f"Extras: {', '.join(extras)}")
  if details:
    print(f"Details: {details}")

# book_ticket("Paris", extras=["window seat", "meal"], discount=10, price=100)  # Extras given as kw argument

book_ticket("Italy", 800)
book_ticket("USA", 1500, 20, "Condition", "Near window", backflip="In 10 days")