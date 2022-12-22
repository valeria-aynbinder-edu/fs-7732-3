class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Triangle(Shape):
    pass


class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Circle(Shape):
    pass
