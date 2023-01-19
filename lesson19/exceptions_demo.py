# def get_int():
#     num = int(input("insert num:"))
#     return num
import datetime
import math

if __name__ == '__main__':
    try:
        num1 = int(input("insert num1:"))
        num2 = int(input("insert num2:"))
        date = input("Insert date in format dd-mm-yy: ")
        date_as_dt = datetime.datetime.strptime(date, "%d-%m-%y")
        print(date[20])
        res = math.factorial(num1)
        res2 = num1 / num2
        print(res, res2)
    except ValueError as e:
        print("Incorrect input - you must insert a positive number")
        print(e)
    except ZeroDivisionError:
        print("Your second number is 0, can't divide by zero")
    except Exception as e:
        print(e)

    print("bye-bye")

# if __name__ == '__main__':
#     num = input("insert num:")
#     if not num.isdigit():
#         print("error")
#         exit()
#     num = int(num)
#     if num < 0:
#         print("error")
#         exit()
#     res = math.factorial(num)
#     print(res)