import time
from concurrent.futures import ThreadPoolExecutor, Future, as_completed

# send many concurrent requests
import requests

def get_quote(num):
    print(f"Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")


# tip - run in debug mode to better understand what future object has
# def display_quote(f: Future):
#     if f.exception():
#         print(f"Could not get quote {f.result()['id']}")
#     elif f.done():
#         print(f"The quote number {f.result()['id']} is {f.result()['quote']}")


# with ThreadPoolExecutor() as executor:
#     futures = [executor.submit(get_quote, i) for i in range(1, 21)] #not blocking
#     # futures = []
#     # for i in range(1, 11):
#     #     f = executor.submit(get_quote, i)
#     #     futures.append(f)
#
#     for f in futures:
#         f.add_done_callback(display_quote) # non blocking
#         # f.add_done_callback(send_by_mail)
#
#     # f.result() #blocking
# for f in futures:
#     print(f"The quote number {f.result()['id']} is {f.result()['quote']}")
#
# print("Exited context manager")
    # or using map

# here the executor is shut down and all the tasks are completed
# now we can examine all the results


if __name__ == '__main__':
    s = time.perf_counter()
    results = []
    for i in range(100):
        results.append(get_quote(i))
    print(f"Synchronious: {time.perf_counter()-s}")

    results2 = []
    futures = []

    s = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        for i in range(100):
            futures.append(executor.submit(get_quote, i))

    for future in as_completed(futures):
        results2.append(future.result())
    print(f"Asynchronious: {time.perf_counter() - s}")
