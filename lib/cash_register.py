from decimal import Decimal

class CashRegister:
  
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_transaction = []

  def add_item(self, item, price, quantity = 1):
    self.total += price * quantity
    self.last_transaction = [item, price, quantity]
    for _ in range(quantity):
      self.items.append(item)

  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      discounted_total = self.total * ((100 - self.discount) * 0.01)
      self.total = int(discounted_total)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    self.total -= self.last_transaction[1] * self.last_transaction[2]
    for _ in range(self.last_transaction[2]):
      self.items.pop()