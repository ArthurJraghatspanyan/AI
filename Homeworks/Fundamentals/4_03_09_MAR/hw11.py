# Հայտարարել set` բաղկացած ամբողջ թվերից: Set-ում եղած բոլոր կենտ թվերը ջնջել, և ավելացնել տվյալ քանակությամբ զույգ թվեր:

import random

st = {-2, 14, 6, 3, 9, -52, 81}
st_copy = {-2, 14, 6, 3, 9, -52, 81}
odd = set()

for i in st_copy:
  if i % 2 != 0:
    odd.add(i)
    st.remove(i)

print(st)

for _ in range(len(odd)):
  st.add(random.randrange(-98, 98, 2))

print(st)