import time

COUNT = 100_000_000

def countdown(n_from, n_to):
    while n_from > n_to:
        n_from -= 1


if __name__ == '__main__':
    start = time.time()
    countdown(COUNT, 0)
    end = time.time()

    print('Time taken in seconds -', end - start)