def calc_square(num: int) -> int:
    return num ** 2


def calc_cube(num: int) -> int:
    return num ** 3


def sum_numbers(num1: int, num2: int) -> int:
    return num1 + num2


# def perform_calculation(num: int, func: callable) -> int:
#     print("Hello")
#     res = func(num)
#     print("Your result is :", res)
#     return res

def perform_calculation(func: callable, *args) -> int:
    print("Hello")
    num1 = args[0]
    if num1 % 2 == 0:
        res = func(*args)
        print("Your result is :", res)
        return res
    else:
        return None

if __name__ == '__main__':
    # result = calc_square(5)
    # print(result)
    # temp = calc_square
    # calc_square(5)
    # temp(5)
    # perform_calculation(calc_square, 10)
    # perform_calculation(sum_numbers, 10, 22)
    perform_calculation(calc_square, 5)
    perform_calculation(calc_square, calc_square(5))
