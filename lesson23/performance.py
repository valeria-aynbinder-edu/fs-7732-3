import math
import time

def measure_performance(func_to_measure):

    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret_val = func_to_measure(*args, **kwargs)
        end_time = time.time()
        print(f"The function {func_to_measure.__name__} "
              f"took {end_time-start_time} seconds top complete")
        return ret_val

    return wrapper


@measure_performance
def long_running_func(num):
    f_list = []
    for i in range(num):
        f = math.factorial(i)
        f_list.append(f)
    return sum(f_list)

if __name__ == '__main__':
    long_running_func(1000)
    long_running_func(10_000)