from States.state import State

class Dispense(State):
    
    def __init__(self, state='dispense'):
        super().__init__(state)

    def dispense_product(self, vending_machine):
        vending_machine.dispense_to_customer()
    