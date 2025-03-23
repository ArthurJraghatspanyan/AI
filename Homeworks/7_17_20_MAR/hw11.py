# Implement a closure that takes a string as input and allows appending to or resetting the string when the inner function is called.

def outter(st=""):
  def inner(operation, st1):
    nonlocal st
    if operation.lower() == "append":
      st += st1
      return st
    elif operation.lower() == "reset":
      st = st1
      return st
  return inner

st = input("Input your string: ")
operation = input("Enter your operation: ")
