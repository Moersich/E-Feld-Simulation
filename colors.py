BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
RED_APPEND = (255, 100, 100)

class Color:
    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __iter__(self):
        return iter([self.r, self.g, self.b])
    
    def __getitem__(self, index: int):
        return (self.r, self.g, self.b)[index]
    
    def __setitem__(self, index: int, value: int):
        if index == 0:
            self.r = value
        elif index == 1:
            self.g = value
        elif index == 2:
            self.b = value
        else:
            raise IndexError("Index out of range")
        
    def __repr__(self):
        return f"Color({self.r}, {self.g}, {self.b})"
    
    def __str__(self):
        return f"Color({self.r}, {self.g}, {self.b})"
    
    def __eq__(self, other: 'Color') -> bool:
        return self.r == other.r and self.g == other.g and self.b == other.b
    
    def __ne__(self, other: 'Color') -> bool:
        return not self.__eq__(other)
    
    def __add__(self, other: 'Color') -> 'Color':
        return Color(self.r + other.r, self.g + other.g, self.b + other.b)
    
    def __sub__(self, other: 'Color') -> 'Color':
        return Color(self.r - other.r, self.g - other.g, self.b - other.b)
    
    def __mul__(self, other: float) -> 'Color':
        return Color(self.r * other, self.g * other, self.b * other)