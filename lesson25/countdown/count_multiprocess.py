import multiprocessing
from concurrent.futures import ProcessPoolExecutor, as_completed

import time

COUNT = 100_000_000


def countdown(n_from, n_to):
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':
    start = time.time()

    with ProcessPoolExecutor() as executor:
        future1 = executor.submit(countdown, COUNT, COUNT//2)
        future2 = executor.submit(countdown, COUNT//2, 0)
        start = time.time()

    for f in as_completed([future1, future2]):
        pass

    end = time.time()

    print('Time taken in seconds -', end - start)