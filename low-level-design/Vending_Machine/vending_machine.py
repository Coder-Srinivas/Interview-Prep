from inventory import Inventory
from States.idle import Idle
from States.cash_inserted import CashInserted
from States.dispense import Dispense

class VendingMachine:
    
    def __init__(self, inventory: Inventory):
        self.vending_state = Idle()
        self.inventory = inventory
        self.amount = 0
        self.product = None
    
    def insert_cash(self, amount):
        self.vending_state.insert_cash(self, amount)

    def select_product(self, code):
        self.vending_state.select_product(self, code)

    def refund(self):
        self.vending_state.refund(self)

    def dispense_product(self):
        self.vending_state.dispense_product(self)

    def update_amount(self, amount: int):
        if not isinstance(amount, int):
            raise ValueError("Amount should be an integer")
        if amount <= 0:
            raise ValueError("Amount cannot be negative")
        
        self.amount += amount
        if isinstance(self.vending_state, Idle):
            self.updare_vending_state_to_cash_inserted()
    
    def update_product(self, code):
        self.inventory.check_validity(code)
        change = self.caculate_change(code)
        if change < 0:
            raise ArithmeticError(f"Infficient balance for the select item, you are short by ${-change}")
        
        self.product = code
        self.update_vending_state_to_dispense()
    
    def refund_customer(self):
        returned_amount = self.amount
        self.reset()
        print(f"{returned_amount} is refuned back to you")
    
    def reset(self):
        self.amount = 0
        self.product = None
        self.update_vending_state_to_idle()
        
    def dispense_to_customer(self):
        try:
            self.inventory.decrement_quantity(self.product)
            change = self.caculate_change(self.product)
            item = self.inventory.get_item(self.product)
            print(f"${item.name} has been dispensed.")
            print(f"${change} has been refuned back to you.")
            self.reset()
        except ValueError as error:
            print(error)
            self.refund_customer()

    def caculate_change(self, code):
        item = self.inventory.get_item(code)
        return self.amount - item.selling_price

    def update_vending_state_to_idle(self):
        self.vending_state = Idle()
    
    def updare_vending_state_to_cash_inserted(self):
        self.vending_state = CashInserted()
    
    def update_vending_state_to_dispense(self):
        self.vending_state = Dispense()
    
    def print_inventory(self):
        self.inventory.available_items()
    