class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      return self.price if 0 < quantity > 10 else (self.price * 0.1 if 10 <= quantity > 99 else self.price * 0.2)

  def make_purchase(self, quantity):
      pass