def complete_num(n):
  summary = 0
  for i in range(1, n):
    if n % i != 0:
      continue
    else:
      summary += i
  if summary == n:
    return True
  else:
    return False

print(complete_num(6))