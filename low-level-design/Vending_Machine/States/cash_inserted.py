from States.idle import Idle

class CashInserted(Idle):
    def __init__(self, state='cash inserted'):
        super().__init__(state)
    
    def select_product(self, vending_machine, code):
        vending_machine.update_product(code)
    
    def refund(self, vending_machine):
        vending_machine.refund_customer()