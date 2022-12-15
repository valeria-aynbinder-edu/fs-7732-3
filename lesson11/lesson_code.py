# from hw - usd converter
# from hw - bank account
# encapsulation - protected fields + getter / setter


class Car:

    def __init__(self, man: str, mod: str, col, year,
                 fuel_consumption, tank_capacity):
        self.__manufacturer = man
        self.__model = mod
        self.__color = col
        self.year = year
        # liters per 100 km
        self.fuel_consumption = fuel_consumption
        self.tank_capacity = tank_capacity

        self.__km = 0
        self.fuel = 0

    def get_manufacturer(self):
        return self.__manufacturer

    def get_model(self):
        return self.__model

    def get_color(self):
        return self.__color

    def set_color(self, color) -> bool:
        if color in ('red', 'white', 'grey', 'blue'):
            self.__color = color
            return True
        return False

    def __str__(self):
        return f"{self.__manufacturer} {self.__model} {self.__color}"

    def fill_tank(self, liters) -> bool:
        if 0 < liters <= self.tank_capacity - self.fuel:
            self.fuel += liters
            return True
        return False

    def drive(self, km) -> bool:
        if km > 0 and (self.fuel * (100/self.fuel_consumption)) >= km:
            self.__km += km
            self.fuel -= (self.fuel_consumption/100) * km
            return True
        return False

if __name__ == '__main__':
    car_mazda = Car('Mazda', '3', 'white', 2015, 20, 50)
    car_mazda.get_manufacturer()
    print("current color:", car_mazda.get_color())
    car_mazda.set_color('grey')
    print("new color:", car_mazda.get_color())
    # print(car_mazda._Car__manufacturer)
    # car_mazda.km += 90
    #
    # car_mazda.km += 100
    # car_mazda.km = -1000
    # car_mazda.km = "aaaa"
    # car_mazda.manufacturer = "toyota"
    ret_val = car_mazda.drive(100)
    # print(ret_val)
    # car_mazda.fill_tank(10)
    # ret_val = car_mazda.drive(15)
    # print(ret_val)


# car_mazda = Car('Mazda', '3', 'white', 2015, 20, 50)
# car_mazda = Car.__init__(None, 'Mazda', '3',)
# car_toyota = Car('Toyota', 'Yaris', 'red', 2022, 10, 35)
# car_mazda.drive()

# ret_val = car_mazda.fill_tank(30)
# print(f"retval is: {ret_val}, new fuel is mazda: {car_mazda.fuel}")
# print(f"new fuel is toyota: {car_toyota.fuel}")
# ret_val = car_mazda.fill_tank(40)
# print(f"retval is: {ret_val}, new fuel is mazda: {car_mazda.fuel}")
#
# print(isinstance(car_mazda, Car))
# print(car_mazda)

# ret_val = car_mazda.__str__()
# print(ret_val)

# print(car_mazda)

# Car.fill_tank(car_mazda, 10)

# fill tank
# car_mazda.fuel += 50

# l1 = list([3,4,5])
# print(l1)
# print(isinstance(l1, Car))
# l2 = list([5,6,78])
#
# print("type of l1:", type(l1))
# print("type of mazda_car: ", type(car_mazda))

# car_mazda.color = 'yellow'
# print(car_mazda.color)


# car = {}

# car1 = Car()
# car1 = Car("Mazda", "3", "white")
# print(type(car1))
# s1 = set([2,3,4,4])
# l1 = list()
# str1 = str()


# exercise - bank account - use private fields

# polymorphism
# - cat/dog
# - point
# datetime
# datetime exercises

# ravkav

# repr