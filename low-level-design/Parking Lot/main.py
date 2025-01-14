'''
'''
from parking_lot import ParkingLot

parking_lot = ParkingLot(20, 5)

while True:
    print("Choose your input")
    print("1: Park Vehicle")
    print("2: Leave Parking Lot")
    print("3: Get all Registration Numbers of the same color")
    print("4: Get parking slot of a vehicle")
    print("5: Get all parkings slots of vehicles of same color")

    inp = int(input())

    if inp == 1:
        registration_number, color, vehicle_type, entrance = input("Enter your reg no, color, vehicle type and entrance (separated by spaces): ").split()
        vehicle_type = int(vehicle_type)
        entrance = int(entrance)

        parking_lot.park(reg_no=registration_number, color=color, vehicle_type=vehicle_type, entrance_no=entrance
                         )
    elif inp == 2:
        registration_number = input("Enter your reg no: ")
        parking_lot.leave(reg_no=registration_number)
    
    elif inp == 3:
        color = input("Enter your vehicle color: ")
        print(parking_lot.get_registration_numbers(color=color))
    
    elif inp == 4:
        registration_number = input("Enter your reg no: ")
        parking_lot.get_parking_slot(reg_no=registration_number)
    
    elif inp == 5:
        color = input("Enter your vehicle color: ")
        print(parking_lot.get_slot_numbers(color=color))
    
    else:
        print("Please choose your input again: ")
