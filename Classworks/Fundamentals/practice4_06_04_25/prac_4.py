# Create a generator function repeat_element(element, times) that yields the given element a specified number of times.
# Test this generator with different inputs.

def repeat_element(element, times=3):
  if not isinstance(times, int):
    raise TypeError("Times must be integer!")
  if times <= 0:
    raise ValueError(f"Can't iterate in range {times}. Enter greater than 0 value.")
  for _ in range(times):
    yield element

print(list(repeat_element([1, 2, 3])))