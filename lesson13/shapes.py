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
        # raise Exception()

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


class Abs(ABC):
    pass
    # @abstractmethod
    # def bla(self):
    #     pass

a = Abs()


# class Triangle(Shape):
#
#     @staticmethod
#     def is_valid_triangle(a, b, c):



# shape = Shape('cm', 'red')
# rect = Rectangle(5, 7, 'm', 'red')
# c = Circle(5, 'mm', 'blue')
