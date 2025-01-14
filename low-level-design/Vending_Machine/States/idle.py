from States.state import State

class Idle(State):
    def __init__(self, state='idle'):
        super().__init__(state)
    
    def insert_cash(self, vending_machine, amount: int):
        vending_machine.update_amount(amount)