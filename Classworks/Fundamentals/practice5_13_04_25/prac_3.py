# Make a decorator repeat(times) that repeats the function times times.

def repeat(times):
  def outter(fn):
    def inner(*args, **kwargs):
      for i in range(times - 1):
        res = fn(*args, **kwargs)
        print(res)
      return fn(*args, **kwargs)
    return inner
  return outter

@repeat(3)
def mul(a, b):
  return a * b

res = mul(4, 5)
print(res)