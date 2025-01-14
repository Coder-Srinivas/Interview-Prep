from coordinates import Coordinates
from parking_spot import ParkingSpot
from type import Type
from typing import List, Tuple
from collections import defaultdict
import math
import heapq

class Entrance(Coordinates):
    def __init__(self, x: int, y: int, parking_spots: List[ParkingSpot]):
        super().__init__(x, y)
        self.closest_spots_based_on_type = defaultdict(list)
        self._generate_heap(parking_spots=parking_spots)
    
    def _compute_distance(self, coordinate2: Coordinates):
        x_diff = self.get_x() - coordinate2.get_x()
        y_diff = self.get_y() - coordinate2.get_y()

        return math.sqrt((x_diff * x_diff) + (y_diff * y_diff))
    
    def _generate_heap(self, parking_spots: List[ParkingSpot]):
        for spot in parking_spots:
            distance = self._compute_distance(spot)
            heap: List[Tuple[float, ParkingSpot]] = self.closest_spots_based_on_type[spot.get_type()]
            heapq.heappush(heap, (distance, spot))
        return heap

    def get_closest_available_spot(self, type_of: Type):
        heap: List[Tuple[float, ParkingSpot]] = self.closest_spots_based_on_type[type_of.get_type()]

        while heap:
            _, spot = heapq.heappop(heap)
            if spot.is_available():
                return spot
        
        raise ValueError(f"No Parking Slots for type {type_of}")
    
    def add_parking_spot(self, parking_spot: ParkingSpot):
        heap: List[Tuple[float, ParkingSpot]] = self.closest_spots_based_on_type[parking_spot.get_type()]
        distance = self._compute_distance(parking_spot)
        heapq.heappush(heap, (distance, parking_spot))