# Մուտքագրել թիվ, տպել թվի թվանշանները առանձին առանձին էկրանին։ Օրինակ՝ մուտքագրված 5479 թվի համար տպել ‘5’, ‘4’, ‘7’, ‘9’։

def each_digit(n):
  ls = []
  while n != 0:
    ls.append(n % 10)
    n //= 10
  for i in range(len(ls) -1, -1, -1):
    print(ls[i], end=' ')
  print()

each_digit(5479113523)