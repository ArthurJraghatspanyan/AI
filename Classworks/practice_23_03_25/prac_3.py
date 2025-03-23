# Implement a function make_config(key, value) that returns a function which, when called, returns a dictionary with the given key-value pair.

def make_config(key, value):
  di = {}
  def inner():
    nonlocal di
    di[key] = value
    return di
  return inner

result1 = make_config("name", "James")
result2 = make_config("age", 25)
print(result1())
print(result2())