# 4. Unique Product Categories (Dictionaries + Sets)
# Given a list of purchased products and their categories, return the unique product categories bought.

products_and_categories = {
  "Apple": "Fruits",
  "Broccoli": "Vegetables",
  "Macbook": "Electronics",
  "TV": "Electronics",
  "Orange": "Fruits",
  "Tomato": "Vegetables",
  "Apricot": "Fruits"
}

unique_product_categories = set()

for category in products_and_categories.values():
  unique_product_categories.add(category)

print(unique_product_categories)