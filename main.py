class Product:
    def __init__(self, product_id, name, price, quantity):
     self.product_id = product_id
     self.name = name
     self.price = price
     self.quantity = quantity

    def add_stock(self , quantity):
       return quantity +1
    
    def minus_stock(self, quantity):
       if quantity == -1:
        print("Quanity can't be negative")
       
       return quantity -1
    
    def get_total_value(self , price, quantity)
      return price*quantity
    
    def __str__(self):
      return f"{self.name} {self.price} {self.product_id} {self.quantity}"