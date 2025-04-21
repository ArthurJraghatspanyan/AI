# Write a closure that creates a counter. Each call to the inner function should increment the counter by 1
# and return the current count.

def counter_closure():
  counter = 0
  def count():
    nonlocal counter
    counter += 1
    return f"Counter, when function called is: {counter}"
  return count

closure = counter_closure()
print(closure())
print(closure())
print(closure())