# Write a decorator greet_decorator that adds a greeting message before and after the execution of the decorated function.

def greet_decorator(fn):
  def inner():
    print("Hello")
    fn()
    print("Goodbye!")
    return fn
  return inner

@greet_decorator 
def say_name(): 
  print("My name is Python.")
say_name()

# Output: 
# Hello! 
# My name is Python. 
# Goodbye!