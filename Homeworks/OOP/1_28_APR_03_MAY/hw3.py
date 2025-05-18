# Create a class BankAccount with account_number and balance. Add a method deposit(amount) to increase the balance

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

account = BankAccount(123, 100)
print(account.balance)
account.deposit(50)
print(account.balance)