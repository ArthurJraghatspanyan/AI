# Task 3: Performance Check

import time

class WithSlots:
  __slots__ = ()

class WithoutSlots:
  pass

def time_with_slots():
  start = time.time()
  for _ in range(100000):
    WithSlots()
  end = time.time()
  return f"Time with slots: {end - start:.6f}"

def time_without_slots():
  start = time.time()
  for _ in range(100000):
    WithoutSlots()
  end = time.time()
  return f"Time without slots: {end - start:.6f}"

print(time_with_slots())      # Faster, because __slots__ prevents direct modification on object __dict__
print(time_without_slots())   # Slower