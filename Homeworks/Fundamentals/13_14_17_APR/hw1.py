# Write a decorator repeat that repeats the execution of the decorated function n times, where n is provided as an argument to the decorator.

def repeat(times):
  def decorator(fn):
    def inner(*args, **kwargs):
      for _ in range(times - 1):
        fn(*args, **kwargs)
      return fn(*args, **kwargs)
    return inner
  return decorator

@repeat(3) 
def greet(): 
  print("Hello!")

greet()

# Output:
# Hello!
# Hello!
# Hello!