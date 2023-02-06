# # Generators - a quick way to write iterators
# # Generator function contains one or more yield statements.
# #
# # When called, it returns an object (iterator) but does not start execution immediately.
# # Methods like iter() and next() are implemented automatically. So we can iterate through the items using next().
# # Once the function yields, the function is paused and the control is transferred to the caller.
# # Local variables and their states are remembered between successive calls.
# #
# # Finally, when the function terminates, StopIteration is raised automatically on further calls.
# from typing import Iterable
#
# num = 10
# # A simple generator function
# def my_gen():
#     global num
#     num += 1
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n
#     print("after first yield")
#
#     n += 1
#     print('This is printed second')
#     yield n
#
#     n += 1
#     print('This is printed at last')
#     yield n
#
#
# # It returns an object but does not start execution immediately.
# # a = my_gen()  # iter(MyNumbers)
#
# # # We can iterate through the items using next().
# # val1 = next(a)
# # print(val1)
#
# # b = my_gen()
# # print(next(b))
#
#
# # Once the function yields, the function is paused and the control is transferred to the caller.
# # Local variables and theirs states are remembered between successive calls.
# # next(a)
# #
# # next(a)
# #
# # # Finally, when the function terminates, StopIteration is raised automatically on further calls.
# # next(a)
#
# #
# # # or using for
# # for i in my_gen():
# #   print(i)
#
# def my_range(start, end, step=1):
#     i = start-1
#     while i < end:
#         i += step
#         yield i
#
#
# for n in my_range(1, 20):
#     print(n)
#
#
# print(list(my_range(1, 20)))
# # list()
#
# def my_list(some_iterable: Iterable):
#     ret_lis = []
#     for i in some_iterable:
#         ret_lis.append(i)
#     return ret_lis



