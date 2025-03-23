# Հայտարարել երկու set: Տպել դրանց միավորումը, հատումը, սիմետրիկ տարբերությունը:

st1 = {1, 2, 3, 4}
st2 = {4, 5, 6, 7}

print(st1 | st2)
print(st1 & st2)
print(f"Symmetric difference 1: {(st1 | st2) - (st1 & st2)}")
print(f"Symmetric difference 2: {(st1 - st2) | (st2 - st1)}")