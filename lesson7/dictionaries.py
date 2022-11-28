# # mapping / dictionary
# countries2cities = {
#     'Israel': 'Jerusalem',
#     'France': 'Paris',
#     'UK': 'London',
#     # 'France': 'Lyon'
# }
# print(countries2cities['UK'])
# print(countries2cities)
# countries2cities['UK'] = 'aaa'
# print(countries2cities)
# countries2cities['USA'] = 'Washington DC'
# print(countries2cities)
# countries2cities.pop('UK')
# print(countries2cities)
# print(len(countries2cities))
# countries2cities['Italy'] = 'Paris'
# print(countries2cities)
# countries2cities['UK'] = None
# print(countries2cities)
#
# stocks = {
#     ('AAPL', '11.11.2022'): 304.5,
#     ('AAPL', '12.11.2022'): 306.8,
#     ('TSLA', '11.11.2022'): 405.8
# }
# print(stocks[('AAPL', '12.11.2022')])

grades = {
    'Nadav': [100, 99, 98, 99],
    'Noam': [98, 99, 99, 98],
    'Daniel': [98, 100, 98]
}

print(grades['Noam'][-1])
grades['Noam'].append(100)
print(grades['Noam'])

grades['Idan'] = [100, 99, 98]
print(grades)

# grades['Herut'] = []

# USD to currency
rates = {
    'NIS': 3.5,
    'EURO': 0.98,
    'YEN': 13500,
}
# print(rates['NIS'])
# currency = input("Insert your currency: ")
# amnt_in_usd = int(input("Insert amnt in usd: "))
# if currency in rates:
#     print(f"You will get {rates[currency]*amnt_in_usd} {currency}")
# else:
#     print("We don't have this currency!")

print(rates.get('tt'))
print(grades)

name = input("Insert name: ")
print(len(grades.get(name, [])))