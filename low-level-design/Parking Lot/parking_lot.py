from entrance import Entrance
from vehicle import Vehicle
from parking_spot import ParkingSpot
from type import Type
from typing import List, Dict
import math

class ParkingLot:

    def __init__(self, total_spots: int, parking_rate: int, entrances: list = [], parking_spots: list = []):
        self.parking_spots: List[ParkingSpot] = []
        self.entrances: Dict[int, Entrance] = {}
        self.assigned_spots: Dict[str, ParkingSpot] = {}
        self.parking_rate = parking_rate
        
        if parking_spots == []:
            self.generateParkingSpots(total_spots)
        else:
            for spot_type, x, y in parking_spots:
                self.parking_spots.append(ParkingSpot(spot_type=spot_type, x=x, y=y))
        
        if entrances == []:
            self.entrances[1] = Entrance(0, 0, parking_spots=self.parking_spots)
        else:
            for index, entrance in enumerate(entrances):
                self.entrances[index+1] = Entrance(entrance[0], entrance[1], parking_spots=self.parking_spots)
        
    def generateParkingSpots(self, total_spots: int):
        root = math.floor(math.sqrt(total_spots))
        counter = 0
        for x in range(1, root+1):
            for y in range(1, root+1):
                spot_type = counter%3 + 1
                counter += 1
                self.parking_spots.append(ParkingSpot(spot_type=spot_type, x=x, y=y))

        remaining = total_spots - (root * root)
        for y in range(remaining):
            spot_type = counter%3 + 1
            counter += 1
            self.parking_spots.append(ParkingSpot(spot_type=spot_type, x=(root+1), y=y))
    
    def park(self, reg_no, color, vehicle_type, entrance_no):
        entrance = self.entrances[entrance_no]

        try:

            empty_spot = entrance.get_closest_available_spot(type_of=Type(vehicle_type))
            vehicle = Vehicle(registration_no=reg_no, color=color, vechile_type=vehicle_type)
            empty_spot.assign_parking_spot(vehicle=vehicle)
            self.assigned_spots[reg_no] = empty_spot
            print(f"Pleae park at {empty_spot.get_x()}, {empty_spot.get_y()}")

        except ValueError as error:
            print(error)
        
    def get_parking_slot(self, reg_no:str):
        if reg_no not in self.assigned_spots:
            print(f"Vehicle with the registration number {reg_no} was not parked")
        
        spot = self.assigned_spots[reg_no]
        print(f"Vehicle is parked at {spot.get_x()}, {spot.get_y()}")
        return spot
    
    def leave(self, reg_no: str):
        spot = self.get_parking_slot(reg_no=reg_no)
        fee = spot.empty_parking_spot(parking_rate=self.parking_rate)
        for entrance in self.entrances.values():
            entrance.add_parking_spot(spot)
        del self.assigned_spots[reg_no]
        print(f"Please make a payment of {fee}")
    
    def get_slot_numbers(self, color:str):
        spots_with_same_color = []
        for spot in self.assigned_spots.values():
            vehicle = spot.get_parked_vehicle()
            if vehicle.get_color() == color:
                spots_with_same_color.append((spot.get_x(), spot.get_y()))
        
        return spots_with_same_color
    
    def get_registration_numbers(self, color:str):
        vehicles_with_same_color = []
        for spot in self.assigned_spots.values():
            vehicle = spot.get_parked_vehicle()
            if vehicle.get_color() == color:
                vehicles_with_same_color.append(vehicle.get_registration_number())
        
        return vehicles_with_same_color
    
    