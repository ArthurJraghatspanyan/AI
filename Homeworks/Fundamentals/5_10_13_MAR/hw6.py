# Write a function greet_with_message that takes a name and an optional message. The default message should be "Welcome!".

# greet_with_message("Alice") # Default message greet_with_message("Bob", "Good morning!") # Custom message

def greet_with_message(name, message = "Welcome!"):
  print(message, name)

greet_with_message("Alice")

greet_with_message("Bob", "Good morning!")