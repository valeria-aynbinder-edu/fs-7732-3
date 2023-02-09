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

def measure_performance2(ms=False):
    def func1(original_function):
        def func2(*args, **kwargs):
            start_time = time.time()
            ret_val = original_function(*args, **kwargs)
            end_time = time.time()
            result = end_time - start_time
            prefix = ""
            if ms:
                result *= 1000
                prefix = "mili-"

            print(f"The function {original_function.__name__} "
                  f"took {result} {prefix}seconds top complete")
            return ret_val
        return func2

    return func1

@measure_performance2(ms=True)
def short_running():
    pass

@measure_performance2(ms=False)
def long_running_func(num):
    f_list = []
    for i in range(num):
        f = math.factorial(i)
        f_list.append(f)
    return sum(f_list)
# long_running_func = measure_performance(long_running_func)
# long_running_func = measure_performance(ms=True)(long_running_func)
# long_running_func = func1(long_running_func)
# func2 = func1(long_running_func)

if __name__ == '__main__':
    long_running_func(1000)
    long_running_func(5000)