import time
from threading import Thread

COUNT = 100_000_000

def countdown(n_from, n_to):
    print(COUNT)
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':
    t1 = Thread(target=countdown, args=(COUNT, COUNT//2))
    t2 = Thread(target=countdown, args=(COUNT//2, 0))

    start = time.time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    end = time.time()

    print('Time taken in seconds -', end - start)