# Մուտքագրել թիվ, տպել թվի թվանշանները առանձին առանձին էկրանին։ Օրինակ՝ մուտքագրված 5479 թվի համար տպել ‘5’, ‘4’, ‘7’, ‘9’։

def each_digit(n):
  for i in str(n):
    print(i, end=', ')

each_digit(5479)