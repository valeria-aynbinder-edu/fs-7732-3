import time

import requests


def get_quote(num):
    print(f"Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")

if __name__ == '__main__':
    result = []
    start = time.time()
    for i in range(100):
        result.append(get_quote(i))
    end = time.time()
    print(f"Second: {end-start}")
    # print(result)