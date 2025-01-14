class Item:
    def __init__(self, name: str, cost_price: int, selling_price: int, code: int, quantity: int):
        self.name = name
        self.cost_price = cost_price
        self.selling_price = selling_price
        self.code = code
        self.quantity = quantity
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def update_selling_price(self, new_price):
        self.selling_price = new_price
    
    def update_cost_price(self, new_price):
        self.cost_price = new_price
    
    def update_name(self, new_name):
        self.name = new_name
    
    def __str__(self):
        return f"{self.name} ${self.selling_price}, item code: {self.code} availability: {self.quantity}"

