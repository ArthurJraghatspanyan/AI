# Պետք է այնպիսի կոդ գրենք, որ միևնույն key-ից մի քանի հատ կարողանանք ունենալ dict-ի մեջ

class Person:
  def __init__(self, name="Arthur"):
    self.name = name
  def __repr__(self):
    return self.name

obj1 = Person()
obj2 = Person()
obj3 = Person()

di = {obj1: 1, obj2: 2, obj3: 3}

print(di)

print()

# Պետք է այնպիսի տիպ ստեղծենք, որ այդ տիպի օբյեկտից լինի ընդամենը մեկ հատ,այսինքն ինչքան այդ տիպի օբյեկտ սարքենք լինի միևնույն օբյեկտը

class Singleton:
  _instance = None
  def __new__(cls):
    if not cls._instance:
      cls._instance = object.__new__(cls)
    return cls._instance

single = Singleton()
print(single)
single2 = Singleton()
print(single2)
single3 = Singleton()
print(single3)

print(single is single2 is single3)