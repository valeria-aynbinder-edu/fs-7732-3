import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

import requests


def get_quote(num):
    if num == 5:
        raise Exception()
    print(f"Worker started - Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(f"worker {num} finished working")
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")


if __name__ == '__main__':
    s = time.time()
    with ThreadPoolExecutor(3) as executor:
        futures = []
        for i in range(10):
            future = executor.submit(get_quote, i)
            futures.append(future)

        print("All tasks submitted")

        results = []
        for future in as_completed(futures):
            if future.exception():
                print("error", future.exception())
            result = future.result()
            results.append(result)
    e = time.time()
    print(e-s)

