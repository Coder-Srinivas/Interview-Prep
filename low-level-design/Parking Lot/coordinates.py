class Coordinates:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y
    
    def set_x(self, x: int):
        self._x = x
    
    def set_y(self, y: int):
        self._y = y

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y