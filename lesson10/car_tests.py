from lesson10.car import Car


def test_negative_values():
    car = Car("Lamborgini", "Diablo", "yellow", 2020, 20, 45)
    km_before = car.km
    ret_val = car.drive(-90)
    assert not ret_val, "Can't insert negative km"
    assert km_before == car.km, "km was changed when received negative km"

def test_correct_fuel_calculation():
    car = Car("Lamborgini", "Diablo", "yellow", 2020, 20, 45)
    assert car.fill_tank(30)
    assert car.fuel == 30
    assert car.drive(100)
    assert car.fuel == 10

if __name__ == '__main__':
    test_negative_values()
    test_correct_fuel_calculation()