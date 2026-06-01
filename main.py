import time

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    
    def add_stock(self, quantity):
        self.quantity += quantity

    
    def minus_stock(self, quantity):
        if self.quantity - quantity < 0:
            print("Quantity can't be negative")
        else:
            self.quantity -= quantity

    def get_total_value(self, price, quantity):
        return price * quantity

    def __str__(self):
        return f" Name: {self.name} |  Price:  ${self.price}  |  ID:  {self.product_id} |  Quantity:  {self.quantity}"


class Inventory:
    
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        self.products[product.product_id] = product

    
    def restock(self, product_id, amount):
        self.products[product_id].add_stock(amount)

    
    def sell_product(self, product_id, amount):
        self.products[product_id].minus_stock(amount)

    def display_all(self):
        for product in self.products.values():
            print(product)


if __name__ == "__main__":
    inventory = Inventory()
    while True:
        print("Welcome to the Inventory System Manager!")
        time.sleep(1)
        print("\n1. Add product")
        print("2. View products")
        print("3. Restock product")
        print("4. Sell product")
        print("5. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            product_id = input("Enter ID: ")
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: ")) 
            product = Product(product_id, name, price, quantity)
            inventory.add_product(product)

        elif choice == "2":
              inventory.display_all()

        elif choice == "3":
              product_id = input("Enter ID: ")
              amount = int(input("Enter Amount: "))
              inventory.restock(product_id, amount)

        elif choice == "4":
              product_id = input("Enter ID: ")
              amount = int(input("Enter Amount"))
              inventory.sell_product(product_id, amount)

        elif choice == "5":
          
          print("Exiting...")
          break

            
        