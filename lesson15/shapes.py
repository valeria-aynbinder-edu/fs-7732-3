import math
from abc import ABC, abstractmethod


class Shape(ABC):

    def __init__(self, units: str, color: str):
        self._units = units
        self._color = color

    def get_color(self):
        return self._color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):

    def __init__(self, height, width, units, color):

        super().__init__(units, color)

        self._height = height
        self._width = width

    def area(self):
        return self._height * self._width

    def perimeter(self):
        return 2 * (self._height + self._width)


class Circle(Shape):

    def __init__(self, radius, units, color):

        super().__init__(units, color)

        self._radius = radius

    def area(self):
        return math.pi * (self._radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self._radius


if __name__ == '__main__':
    # my_shape = Shape('mm', 'red')
    r1 = Rectangle(3, 4, 'mm', 'white')
    r2 = Rectangle(13, 40, 'cm', 'white')
    r3 = Rectangle(3, 5, 'm', 'red')
    c1 = Circle(5, 'mm', 'green')
    c2 = Circle(6, 'cm', 'black')

    shapes = [r1, r2, r3, c1, c2]

    for s in shapes:
        print(s.area())