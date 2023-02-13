import multiprocessing
from concurrent.futures import ProcessPoolExecutor

import time

COUNT = 100_000_000


def countdown(n_from, n_to):
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':
    start = time.time()

    p1 = multiprocessing.Process(target=countdown, args=(COUNT, COUNT//2))
    p2 = multiprocessing.Process(target=countdown, args=(COUNT//2, 0))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()
    print('Time taken in seconds -', end - start)

    executor = ProcessPoolExecutor()