# Implement a function make_greeting(greeting) that takes a greeting string and returns a function that takes
# a name and prints the greeting followed by the name.

def make_greeting(greeting):
  def inner(name):
    return f"{greeting}, {name}"
  return inner

result = make_greeting("Hello")
print(result("Arthur!"))