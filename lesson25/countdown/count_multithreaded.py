import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread

COUNT = 100_000_000

def countdown(n_from, n_to):
    print(COUNT)
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':

    with ThreadPoolExecutor(max_workers=10) as executor:
        future1 = executor.submit(countdown, COUNT, COUNT//2)
        future2 = executor.submit(countdown, COUNT//2, 0)
        start = time.time()

    for f in as_completed([future1, future2]):
        pass

    end = time.time()

    print('Time taken in seconds -', end - start)