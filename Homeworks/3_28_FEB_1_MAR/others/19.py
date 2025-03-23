# Հայտարարել list և տպել նվազագույն արժեքով էլեմենտի ինդեքսը։

import random

ls = [random.randint(i, 100) for i in range(10)]
min = ls[0]
min_index = 0

for i in range(1, len(ls)):
  if ls[i] < min:
    min_index = i

print(f"Minimum index in {ls} is: {min_index}")