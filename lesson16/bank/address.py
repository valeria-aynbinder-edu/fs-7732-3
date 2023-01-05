class Address:
    def __init__(self, country, city, street,
                 zip_code, building_num, entrance=None, floor=None):
        self._floor = floor
        self._entrance = entrance
        self._building_num = building_num
        self._zip_code = zip_code
        self._street = street
        self._city = city
        self._country = country

    def get_city(self):
        return self._city
