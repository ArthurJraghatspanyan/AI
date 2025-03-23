# Հայտարարել list, և տպել list-ի էլեմենտներից առավելագույնի արժեքը:
# List-ը պետք է պարունակի միայն int տիպի արժեքներ: Չօգտագործել max ֆունկցիան:

import random

ls = [random.randint(i, 100) for i in range(10)]
max = ls[0]

for i in range(1, len(ls)):
  if ls[i] > max:
    max = ls[i]

print(f"Maximum value in {ls} is: {max}")