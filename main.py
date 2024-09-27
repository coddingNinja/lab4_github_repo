class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      return self.price * quantity if 0 < quantity > 10 else (self.price * 0.1 * quantity if 10 <= quantity > 99 else self.price * 0.2 * quantity)

  def make_purchase(self, quantity):
      self.amount -= quantity
      return get_price(quantity=quantity)