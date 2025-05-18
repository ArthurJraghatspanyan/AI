# Create a decorator log_execution that logs the name of the function being executed along with its arguments
# and return value.

def log_execution(fn):
  def inner(*args, **kwargs):
    print(f"Executing add with arguments {args} and {kwargs}")
    print(f"add returned {fn(*args, **kwargs)}")
    return fn(*args, **kwargs)
  return inner

@log_execution
def add(a, b):
  return a + b

add(3, 5)

# Output: 
# Executing add with arguments (3, 5) and {}
# add returned 8