#sp23-bai-006
#sp23-bai-018

from exception import OutOfStockException

class Product:
  def __init__(self, name, amount, price):
      self.name = name
      self.amount = amount
      self.price = price

  def get_price(self, quantity):
      return self.price * quantity if 0 < quantity > 10 else (self.price * 0.1 * quantity if 10 <= quantity > 99 else self.price * 0.2 * quantity)

  def make_purchase(self, quantity):
      if quantity<self.amount:
          raise OutOfStockException(Quantity=quantity, Amount=self.amount)
      self.amount -= quantity
      return self.get_price(quantity=quantity)
  
product1 = Product("Laptop", 10, 500)
product2 = Product("Phone", 20, 300)
product3 = Product("Headphones", 50, 100)


try:
    price = product1.make_purchase(quantity=1)
    print(price)
except OutOfStockException as e:
    print(e)

  