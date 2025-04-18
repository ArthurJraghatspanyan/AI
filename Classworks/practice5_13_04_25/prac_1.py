# Write a function my_decorator that wraps another function and prints "Function is called" before it runs.

def my_decorator(fn):
  def inner():
    fn()
  return inner

def say_hello():
  print("Hello, World!")

res = my_decorator(say_hello)
res()