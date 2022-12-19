import datetime


def my_test(n: int):
    prod = 1
    for i in range(n):
        prod = prod * n

if __name__ == '__main__':
    start = datetime.datetime.now()
    my_test(100000)
    end = datetime.datetime.now()
    run_time = (end - start).total_seconds()
    print(run_time)