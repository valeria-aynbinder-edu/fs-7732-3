import json

import requests

if __name__ == '__main__':
    bored_url = "https://www.boredapi.com/api/activity"
    response = requests.get(bored_url)
    print(response)
    if response.status_code == 200:
        my_data = response.json()
        print(my_data)
        print(type(my_data))

    # print(f"the type of response.text: {type(response.text)}")
    # response_as_dict = json.loads(response.text)
    # print(f"the type of response_as_dict: {type(response_as_dict)}")
    # print(f"Activity: {response_as_dict['activity']}")
    # print(response.text['activity'])
    # print(type(response))