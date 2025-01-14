class Type:

    types = {1: 'small', 2: 'medium', 3: 'large'}
    def __init__(self, type_of: int):
        self._type = type_of

    def get_type(self):
        return self.types[self._type]
    
    def set_type(self, type_of: int):
        self._type = type_of
    
    @classmethod
    def get_types(cls):
        return cls.types
