import time
from threading import Thread

import requests


def get_quote(num):
    time.sleep(2)
    print(f"Worker started - Getting quote {num}")
    response = requests.get("https://api.kanye.rest")
    if response.status_code < 400:
        print(f"worker {num} finished working")
        return {'id': num, 'quote': response.json()['quote']}
    else:
        raise Exception(f"Received response code {response.status_code} for quote {num}")

def wait():
    time.sleep(3)

if __name__ == '__main__':
    thread1 = Thread(target=get_quote, args=(1, ))
    thread1.start()

    thread2 = Thread(target=get_quote, args=(2, ))
    thread2.start()

    print("before join1")
    thread1.join()
    print("after join1, before join2")
    thread2.join()
    print("after join2")


