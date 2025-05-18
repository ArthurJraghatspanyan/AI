# Create a dictionary to represent a store’s inventory with items as keys and quantities as values.
# Print the quantity of a specific item (e.g., "Apples").
# Update the quantity of an item and print the dictionary to show the change.

di = {
  "Apples": 90,
  "Strawberries": 200,
  "Oranges": 50
}

print(di["Apples"])

di.update({"Oranges": 60})

print(di)