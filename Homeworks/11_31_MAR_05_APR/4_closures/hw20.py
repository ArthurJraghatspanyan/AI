# Implement a closure that takes a string as input and allows appending to or resetting the string when the
# inner function is called.

def closure(st=""):
  def inner(operation, st1):
    nonlocal st
    if not isinstance(st1, str):
      raise TypeError("Type must be string")
    if operation.lower() == "append":
      st += st1
      return st
    elif operation.lower() == "reset":
      st = st1
      return st
    else:
      return -1
  return inner

st = input("Input your string: ")
operation = input("Enter your operation: ")

res = closure(st)
print(res(operation, "world"))