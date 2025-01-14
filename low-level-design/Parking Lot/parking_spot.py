"""This module defines the parking spot class."""
from datetime import datetime
from type import Type
from coordinates import Coordinates
from vehicle import Vehicle

class ParkingSpot(Type, Coordinates):
    def __init__(self, spot_type: Type, x: int, y: int, timestamp=None, parked_vechile: Vehicle = None):
        super().__init__(spot_type)
        Coordinates.__init__(self, x, y)
        self._timestamp = timestamp
        self._parked_vechile = parked_vechile

    def is_available(self):
        return not self._parked_vechile
    
    def get_timestamp(self):
        return self._timestamp
    
    def set_timestamp(self, timestamp: datetime):
        self._timestamp = timestamp

    def assign_parking_spot(self, vehicle: Vehicle):
        self.set_timestamp(datetime.now())
        self._parked_vechile = vehicle
    
    def get_parked_vehicle(self):
        return self._parked_vechile
    
    def compute_parking_fee(self, leaving_timestamp: datetime, parking_rate: float):
        time_parked = leaving_timestamp - self.get_timestamp()
        total_hours = time_parked.total_seconds() / 3600

        return parking_rate * total_hours
    
    def empty_parking_spot(self, parking_rate: float):
        fee = self.compute_parking_fee(datetime.now(), parking_rate)
        self.set_timestamp(None)
        self.assign_parking_spot(None)
        return fee
    
    def __lt__(self, other):
        return self.get_x() < other.get_x()