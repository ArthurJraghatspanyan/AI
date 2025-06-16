# Task 4: Singleton Pattern with __new__

class Config:
  _instance = None
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls, *args, **kwargs)
    return cls._instance

obj1 = Config()
obj2 = Config()
obj3 = Config()

print(obj1 == obj2 == obj3)     # Comparison by addresses