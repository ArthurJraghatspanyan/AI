#Implement a decorator ensure_unique_call that prevents a function from being called with the same arguments more than once
#If called with the same arguments, it should return the previous result.

def ensure_unique_call(fn):
  cache = {}
  def inner(*args, **kwargs):
    nonlocal cache
    key = (args + tuple(sorted(kwargs)))
    if key in cache:
      return f"Arguments repeated. Result is the previous: {cache[key]}"
    cache[key] = fn(*args, **kwargs)
    return fn(*args, **kwargs)
  return inner

@ensure_unique_call
def add(x, y):
  return x * y

print(add(4, 5))
print(add(4, 5))
print(add(4, 6))