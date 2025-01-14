from item import Item
from inventory import Inventory
from vending_machine import VendingMachine

coke = Item('Coke', 0.5, 2, 1, 10)
pepsi = Item('Pepsi', 0.5, 2, 2, 10)
sprite = Item('Sprite', 0.5, 2, 3, 10)
lays = Item('Lays', 1, 3, 4, 10)
doritos = Item('Doritos', 1, 3, 5, 10)
fritos = Item('Fritos', 1, 3, 6, 10)
twix = Item('Twix', 2, 4, 7, 10)
kinder = Item('Kinder', 2, 3, 8, 10)
burger = Item('Burger', 2, 5, 9, 10)

items = [coke, pepsi, sprite, lays, doritos, fritos, twix, kinder, burger]
inventory = Inventory(items=items)
vending_machine = VendingMachine(inventory=inventory)

print("Welcome to our Vending Machine")
valid_options = [1, 2, 3, 4]

while True:

    try:
        vending_machine.print_inventory()
        print("1. Insert Cash")
        print("2. Select Product")
        print("3. Dispense Product")
        print("4. Refund")
        user_input = int(input("Choose a value "))

        if user_input not in valid_options:
            print("Incorrect option selected. please try again")
            continue
        
        if user_input == 1:
            amount = int(input("Enter the amount inserted "))
            vending_machine.insert_cash(amount)

        elif user_input == 2:
            code = int(input("Enter the product code "))
            vending_machine.select_product(code)
        
        elif user_input == 3:
            vending_machine.dispense_product()
        
        else:
            vending_machine.refund()
    
    except Exception as error:
        print("\033[91m" + str(error) + "\033[0m")

