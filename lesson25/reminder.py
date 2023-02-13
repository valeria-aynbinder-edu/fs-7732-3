import datetime
import time
from concurrent.futures import ThreadPoolExecutor

import requests


def get_quote(num):
    time.sleep(15)
    print(f"Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")

def get_quote_error(num):
    print(f"Getting quote {num}")
    response = requests.get("https://api.kanye.rest1")
    if response.status_code < 400:
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")



if __name__ == '__main__':

    with ThreadPoolExecutor(2) as executor:

        # future1 = executor.submit(get_quote, 1)


        # for i in range(5):
        #     print("is done:", future1.done())
        # print("start waiting for result", datetime.datetime.now())
        # try:
        #     result = future1.result(timeout=5)
        #     print("is done:", future1.done(), datetime.datetime.now())
        #     print("finished waiting for result")
        #     print(result)
        # except TimeoutError:
        #     print("Timed out", datetime.datetime.now())

        future2 = executor.submit(get_quote_error, 2)

        exc = future2.exception()
        if exc:
            print("error occured", exc)
        else:
            res = future2.result()
            print(res)
