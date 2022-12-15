import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def translate(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        print("inside __eq__ of Point2D")
        if not isinstance(other, Point2D):
            return False
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        print("inside __ne__ of Point2D")
        return self.x != other.x or self.y != other.y

    def __add__(self, other):
        if not isinstance(other, Point2D):
            return None
        new_point = Point2D(self.x + other.x, self.y + other.y)
        return new_point
        # error, don't do it:
        # return (self.x + other.x, self.y +other.y)

    # def distance_from(self, other):
    #     dx = self.__x - other.__x
    #     dy = self.__y - other.__y
    #     dist = math.sqrt(dx ** 2 + dy ** 2)
    #     return dist
    #
    # def __str__(self):
    #     return f"({self.__x},{self.__y})"
if __name__ == '__main__':
    p1 = Point2D()
    p2 = Point2D(2, 5)
    print(p1, p2)
    p2.translate(-2, -2)
    p1.translate(3, 3)
    print(p1)
    print(p2)
    p3 = Point2D(0, 3)
    print(f"p1: {p1}, p2: {p2}, p3:{p3}")
    print(f"p2 == p3: {p2 == p3}")
    print(f"p2 == p1: {p2 == p1}")
    print(f"p2 != p3: {p2 != p3}")
    print(p2 == "hello")
    # print("hello" == 'world')
    p5 = p2 + p3
    print(p5)
    # p5 :Point (p2.x+p3.x, p2.y + p3.y)

    # s1 = input()
    # s2 = input()
    # print(s1 == s2)
    # print(s1 is s2)

