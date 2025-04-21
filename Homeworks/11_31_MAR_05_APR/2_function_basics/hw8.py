# Write a function personal_greeting that takes a required name argument and an optional greeting argument.
# The default greeting should be "Hi".

def personal_greeting(name, greeting="Hi"):
  return f"{greeting}, {name}!"

print(personal_greeting("Arthur"))