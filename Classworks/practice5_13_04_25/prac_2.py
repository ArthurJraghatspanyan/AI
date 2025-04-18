# Write a decorator log_args that prints the arguments and keyword arguments passed to a function.

def log_args(fn):
  def inner(*args, **kwargs):
    print(args)
    print(kwargs)
    return fn
  return inner

def add(a, b):
  return a + b

res = log_args(add)
res(4, b=5)