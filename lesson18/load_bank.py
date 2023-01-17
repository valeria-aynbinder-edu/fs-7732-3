import pickle
from pickle_example import *


if __name__ == '__main__':
    with open("data/bank.pickle", "rb") as f:
        ret_val = pickle.load(f)
    print(type(ret_val))