# sliding_window(iterable, window_size)
# Yield a sliding window of the given size from the iterable.
# Example: sliding_window([1,2,3,4], 3) → yields (1,2,3), (2,3,4)

import typing

def sliding_window(iterable, window_size=1):
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Type must be iterable.")
  if not iterable:
    return []
  if window_size <= 0:
    raise ValueError("Window size must be greater than 0")
  if len(iterable) < window_size:
    raise ValueError("Iterable size must be greater or equal than window size")
  start = 0
  while window_size <= len(iterable):
    tmp = []
    for i in range(start, window_size):
      tmp.append(iterable[i])
    yield tuple(tmp)
    start += 1
    window_size += 1

print(list(sliding_window([1, 2, 3, 4, 5, 6, 7], 7)))