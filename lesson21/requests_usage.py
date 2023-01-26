import json

import requests

# starting from GET

# sending rewuest to URL

# BORED_URL = "https://www.boredapi.com/api/activity"
# response = requests.get(BORED_URL)
# print(response)
# print(type(response))
# #
# print(response.status_code)
# print(response.text)
# res = json.loads(response.text)
# print(type(res))
# print(response.text['activity']) # not working
#
# response_as_json = response.json()
# print(response_as_json)
# print(response_as_json['activity'])

# response = requests.get("http://www.google.com")
# print(response.status_code)
# print(response.text)
# print(response.json())

# https://www.some_domain.com:80/api/places?place_name=telaviv&country=israel

# response = requests.get("https://bad_url")
# response = requests.get("https://www.boredapi.com/api/act")
# print(response.status_code)
# print(response.text)


# with query param

# GENDERIZE_URL = "https://api.genderize.io"
# response = requests.get(
#     GENDERIZE_URL, params={'name': 'valeria'})
# print(response.status_code, response.text, sep="\n")

# GENDERIZE_URL = "https://api.genderize.io/bla/"
# response = requests.get(GENDERIZE_URL,
#                         params={'name': 'valeria'})
# print(response.status_code, response.text, sep="\n")

# if __name__ == '__main__':
#
#     name = input("Insert your name: ")
#     GENDERIZE_URL = "https://api.genderize.io"
#     response = requests.get(
#         GENDERIZE_URL, params={'name': name})
#     if response.status_code < 400:
#         name_dict = response.json()
#         print(f"Your name is a {name_dict['gender']} name with probability of {name_dict['probability']}%")
#     else:
#         print(f"There is an error: {response.status_code}")
#
#     countries = {"country": [{"country_id": "GH", "probability": 0.224}, {"country_id": "PH", "probability": 0.084},
#                  {"country_id": "NG", "probability": 0.073}, {"country_id": "US", "probability": 0.061},
#                  {"country_id": "NE", "probability": 0.034}], "name": "nathaniel"}
#
#     mx_prob_country = sorted(countries['country'], key=lambda c: c['probability'], reverse=True)[0]
#     print(mx_prob_country)


# with path param
# https://restcountries.com/v3.1/alpha/il
