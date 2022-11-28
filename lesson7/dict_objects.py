# id
# name
# bday
# address
# phone

# person1 = {
#     "id": 123123123,
#     "name": "Valeria",
#     "bday": "11.02.87",
#     "address": "NEtanya",
#     "phone": "054444444"
# }
#
# person2 = {
#     "id": 33333333,
#     "name": "Moshe",
#     "bday": "5.5.90",
#     "address": "Tel Aviv",
#     "phone": "0566666666"
# }
#
# persons = [person1, person2]
# for p in persons:
#     print(p["address"])


fields = ('origin', 'destination', 'price', 'date', 'time')
flights = []
# while True:
#     flight = {}
#     for field in fields:
#         f = input(f"Insert {field}")
#         if f == '$':
#             print(flights)
#             exit(0)
#         flight[field] = f
#     flights.append(flight)
#     print(f"The new flight is: {flight}")

all_flights = [
    {'origin': 'New York',
     'destination': 'Tel Aviv',
     'price': '2345',
     'date': '11.2.2023',
     'time': '11:20'},

    {'origin': 'Paris',
     'destination': 'London',
     'price': '200',
     'date': '11.2.2023',
     'time': '13:00'}
]

# prices_sum = 0
# for flight in all_flights:
#     prices_sum += float(flight['price'])
# print(f"Avg price is {prices_sum/len(all_flights)}")

flights_by_origin = {
    'New York' :     {'origin': 'New York',
                      'destination': 'Tel Aviv',
                      'price': '2345',
                      'date': '11.2.2023',
                      'time': '11:20'},
    'Paris':     {'origin': 'Paris',
                  'destination': 'London',
                  'price': '200',
                  'date': '11.2.2023',
                  'time': '13:00'}
}


flights_by_origin_and_dest = {
    ('New York', 'Tel Aviv') :     {'origin': 'New York',
                      'destination': 'Tel Aviv',
                      'price': '2345',
                      'date': '11.2.2023',
                      'time': '11:20'},
    ('Paris', 'London'):     {'origin': 'Paris',
                  'destination': 'London',
                  'price': '200',
                  'date': '11.2.2023',
                  'time': '13:00'}
}

companies = {

}

print(flights_by_origin['New York']['price'])

# companies['TSLA']['stock_price']['11.11.2022']['open_price']