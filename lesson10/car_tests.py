from lesson10.car import Car


def test_negative_values():
    car = Car("Lamborgini", "Diablo", "yellow", 2020, 20, 45)
    km_before = car.km
    ret_val = car.drive(-90)
    assert ret_val == False, "Can't insert negative km"
    assert km_before == car.km, "km was changed when received negative km"

if __name__ == '__main__':
    test_negative_values()