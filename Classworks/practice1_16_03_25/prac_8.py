def custom_join(ls, sp):
  sentence = ""
  for i in range(len(ls) - 1):
    sentence += ls[i] + sp
  sentence += ls[-1]
  return sentence

ls = ["Hello", "World", "Welcome", "To", "Python", "Bob", "Smith"]
sp = '~~~'
print(custom_join(ls, sp))