# Modify the BankAccount class to include a withdraw(amount) method that reduces the balance if there are enough funds.

class BankAccount:
  def __init__(self, account_number: int, balance: int):
    if not isinstance(account_number, int) or not isinstance(balance, (int, float)):
      raise TypeError("Types must be digit!")
    self.account_number = account_number
    self.balance = balance
  
  def deposit(self, amount: int):
    if not isinstance(amount, (int, float)):
      raise TypeError("Type of amount must be integer or float!")
    if amount <= 0:
      raise ValueError("Amount must be greater than 0!")
    self.balance += amount
  
  def withdraw(self, amount: int):
    if not isinstance(amount, (int, float)):
      raise TypeError("Type of amount must be integer or float!")
    if amount <= 0:
      raise ValueError("Amount must be greater than 0!")
    if amount > self.balance:
      raise ValueError("Not enough funds to make withdraw!")
    self.balance -= amount

account = BankAccount(123, 100)

print(account.balance)
account.deposit(50)
print(account.balance)
account.withdraw(40)
print(account.balance)