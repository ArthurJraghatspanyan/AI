# Write a closure that tracks the number of times a specific function is called.

def function_call_times():
  times = 0
  def count():
    nonlocal times
    times += 1
    return f"Time, when function called is: {times}"
  return count

closure = function_call_times()
print(closure())
print(closure())
print(closure())