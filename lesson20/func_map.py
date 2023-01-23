# map(func, *iterables) --> map object
def foo_squared(num):
    return num**2

my_list = [1, 3, 5, 6]

print(list(map(foo_squared, my_list)))
print(list(map(lambda x: x**2, my_list)))
print(my_list)

words = ['grapes', 'strawberry', 'banana']
words_new = list(map(str.title, words))
print(words_new)

nums1 = [1,2,3,4,5]
nums2 = [10,20,30,40,50]

# new_list = []
# for n1, n2 in zip(nums1, nums2):
#     new_list.append(n1 + n2)

list_of_lists = [(1,2,3), [10,20,30], [100,200,300,400]]

print(list(map(lambda n1, n2, n3: n1 + n2 + n3, nums1, nums2, [100, 200, 300, 400, 500])))
print(list(map(lambda *args: sum(args), nums1, nums2, [100, 200, 300, 400, 500])))
print(list(map(lambda *args: sum(args), *list_of_lists)))

# print(list(map(sum, nums1, nums2)))

def my_sum(*args):
    return sum(args)



# ret_val = list(map(foo_squared, my_list))
#
# print(ret_val)
#

my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS']
# for i in my_list:
    # do this on element
    # do @2 on element

# def my_split(elem):
#     return elem.split(" ")
#
# def my_get_last(elem: list[str]):
#     return elem[-1]
#
# ret_val_from_map = map(my_get_last, map(my_split, map(str.lower, my_list)))
# print(type(ret_val_from_map))
# print(list(ret_val_from_map))
# for i in ret_val_from_map:
#     print(i)

# print(list(ret_val_from_map))

# list(my_list)



# print(list(map(str.lower, ['Apple', 'baNana', 'ANANAS'])))


# you can also pass multiple iterators to map
# def foo_sum(*args):
#     return sum(args)
#
# my_tuple1, my_tuple2 = (1, 2, 3, 4), (10, 20, 30, 40)
# ret_val = map(foo_sum, my_tuple1, my_tuple2, [100, 200, 300, 400])
# print(list(ret_val))



# we want any number of params
# def s(*args):
#     ret_val = 0
#     for a in args:
#         ret_val += a
#     return ret_val
#
# ret_val = map(s, my_tuple1, my_tuple2, (100, 200, 300, 400))
# print(list(ret_val))

# you can pass any existing function, or functions defined in class (method)
# example - map to upper case
# ret_val = map(str.upper, ['a', 'bb', 'ccc'])
# ret_val = map(lambda x: x.upper(), ['a', 'bb', 'ccc'])
# ret_val = []
# for i in ['a', 'bb', 'ccc']:
#     ret_val.append(i.upper())
# print(list(ret_val))


# my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS']
#
# def my_split(elem):
#     return elem.split(" ")
#
# my_split = lambda elem: elem.split(" ")
#
# def my_get_last(elem: list[str]):
#     return elem[-1]
    # if 'a' in elem[-1]:
    #     return elem[-1]
    # else:
    #     return elem[0]
    # return elem[-1] if 'a' in elem[-1] else elem[0]

# ret_val_from_map = map(my_get_last, map(my_split, map(str.lower, my_list)))
# ret_val_from_map = map(lambda x: x[-1],
#                        map(lambda x: x.split(" "),
#                            map(str.lower, my_list)))