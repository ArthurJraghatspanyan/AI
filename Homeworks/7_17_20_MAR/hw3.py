# Write a function order_item that accepts:
# A required item argument.
# A quantity argument with a default value of 1.
# Arbitrary positional arguments (*args) to specify additional options.
# Arbitrary keyword arguments (**kwargs) for customization details.

def order_item(item, quantity = 1, *accessories, **comment):
  invoice = {"Item": item, "Quantity": quantity}
  if quantity < 1:
    return "Quantity must be positive"
  if accessories:
    for acces in accessories:
      invoice["Accessories"] = acces
  if comment:
    for key, value in comment.items():
      invoice[key] = value
  for key, value in invoice.items():
    print(key, ":", value)

order_item("TV")
order_item("TV", 5, ["Remote controller", "Stand for TV"], comment="Bring near to the office, I will meet the courier")