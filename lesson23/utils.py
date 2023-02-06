from typing import Iterable


def batches(n: int, l: Iterable):
    i = 0
    while i < len(l):
        yield l[i: i+n]
        i += n


if __name__ == '__main__':
    my_list = [1,2, 3,4,5,6,7,8,9,10]
    for b in batches(3, my_list):
        print(b)

