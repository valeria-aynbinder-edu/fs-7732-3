# def greet():
#     """
#     Function that greets everyone
#     :return: None
#     """
#     print("Hello All!")
#
# #
# # # Calling a function
# # greet()
# #
# # print(f"Type of greet is: {type(greet)}")
# #
# # print(f"Type of greet is: {type(greet)}\n\n"
# #       f"Some attributes of greet:\n\n"
# #       f"__name__ attribute:\n {greet.__name__}\n\n"
# #       f"__doc__ attribute:\n {greet.__doc__}\n\n"
# #       f"__code__ attribute:\n {greet.__code__}\n\n")
#
#
# # def wrapper(other_function):
# #     print(f"Running function {other_function} received as param...\n")
# #     other_function()
# #
# # # Call wrapper() that will in turn call function passed as parameter
# # wrapper(greet)
#
#
# def wrapper_func():
#     print("Hello")
#     def my_greet():
#         print("Hi")
#         return 9
#
#     return my_greet
#
# print(dir())
#
# a = wrapper_func()
# print(a())
#
# from lesson23.various_functions import factorial, convert_from_farenheit


def greeting_decorator(other_func):

    def greeting_func(*args, **kwrgs):
        print(f"\n---------------------------------------\n"
              f"Hello!\nWelcome to function {other_func.__name__}!\n"
              f"---------------------------------------\n")
        # Note we call the function we received as parameter
        # inside our inner function
        ret_val = other_func(*args, **kwrgs)
        print(f"\n---------------------------------------\n"
              f"Good-bye!\nThanks for using function {other_func.__name__}!"
              f"\n---------------------------------------\n")
        return ret_val

    return greeting_func

# my = greeting_decorator(factorial)
# my()
#
# my = greeting_decorator(convert_from_farenheit)
# my()