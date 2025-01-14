from abc import ABC

class State(ABC):
    def __init__(self, state):
        self.state = state
    
    def insert_cash(self, vending_machine, amount):
        raise NotImplementedError(f"You cannot insert cash in the {self.state} state.")
    
    def select_product(self, vending_machine, code):
        raise NotImplementedError(f"You cannot insert cash in the {self.state} state.")
    
    def dispense_product(self, vending_machine):
        raise NotImplementedError(f"You cannot dispense item in the {self.state} state.")
    
    def refund(self, vending_machine):
        raise NotImplementedError("You cannot ask for a refund when the item is dispencing")