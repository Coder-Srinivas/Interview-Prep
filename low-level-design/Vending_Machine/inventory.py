from item import Item
from typing import Dict, List

class Inventory:

    def __init__(self, items: List[Item]):
        self.items: Dict[int, Item] = {}

        for item in items:
            self.add_item(item)
    
    def add_item(self, item: Item):
        self.items[item.code] = item

    def remove_item(self, code: int):
        self.check_validity(code)
        del self.items[code]
    
    def update_quantity(self, code: int, new_quantity: int):
        self.check_validity(code)
        if new_quantity <= 0:
            raise ValueError("Quantity cannot be negative")
        self.items[code].update_quantity(new_quantity)

    def decrement_quantity(self, code: int):
        self.check_validity(code)
        item = self.items[code]
        if item.quantity < 0:
            raise ValueError(f"There are no more {item}'s available.")
        item.quantity -= 1

    def get_item(self, code):
        self.check_validity(code)
        return self.items[code]
    
    def check_validity(self, code):
        if code not in self.items:
            raise ValueError("Please enter the correct code")
    
    def available_items(self):
        for _, item in self.items.items():
            print(item)
    
    