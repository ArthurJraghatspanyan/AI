# Countdown Generator with Print Statements

def countdown(n):
  gen = (i for i in range(n, -1, -1))
  return gen

res = countdown(5)
print(next(res))
print(next(res))
print(next(res))