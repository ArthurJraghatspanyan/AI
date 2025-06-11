# Task 8: Encapsulation in a Bank Account System

class BankAccount:

  def __init__(self):
    self.__balance = 0
  
  @property
  def balance(self):
    return self.__balance
  
  @balance.setter
  def balance(self, newBalance):
    raise ValueError()

  def deposit(self, amount: int):
    if not isinstance(amount, int):
      raise TypeError("Expected integer.")
    if amount <= 0:
      raise ValueError("Amount must be greater than 0.")
    self.__balance += amount
    print("Deposit made successfully.")
  
  def withdraw(self, amount: int):
    if not isinstance(amount, int):
      raise TypeError("Expected integer.")
    if amount <= 0:
      raise ValueError("Amount must be greater than 0.")
    if amount > self.__balance:
      raise ValueError("Not enough balance to make withdraw.")
    self.__balance -= amount
    print("Withdraw made successfully.")


account = BankAccount()
print(account.balance)
account.deposit(100)
print(account.balance)
account.withdraw(50)
print(account.balance)

account.__balance = 10000
account.__dict__['_BankAccount__balance'] = 1000
print(account.__dict__)
# print(account.__balance)