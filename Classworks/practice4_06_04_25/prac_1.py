# chunk_generator(iterable, size)
#  Yield successive size-sized chunks from an iterable.
 # Example: chunk_generator([1,2,3,4,5,6], 2) → yields (1,2), (3,4),(5,6)

import typing

def chunk_generator(iterable, size):
  if not iterable:
    raise ValueError("Missing iterable")
  if not isinstance(iterable, typing.Iterable):
    raise TypeError("Object must be iterable")
  if not size:
    return []
  if size < 0:
    raise ValueError("Invalid case")
  for i in range(0, len(iterable), size):
    yield iterable[i:size + i]

print(list(chunk_generator([1, 2, 3, 4, 5, 6], 2)))