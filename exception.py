class OutOfStockException(Exception):
    def __init__(self,Quantity,Amount):
        self.Quantity=Quantity
        self.Amount=Amount
        super().__init__(f"Not enouth stock available stock = {Amount}")