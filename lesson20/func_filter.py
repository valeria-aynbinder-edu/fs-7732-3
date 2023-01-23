

words = ["hello", 'hi', "WORLD", "yes", "APPLE", "banana"]
# filtered_list = []
# for w in words:
#     if w.islower():
#         filtered_list.append(w)
# print(filtered_list)

# def my_filter(filter_func: callable, collection) -> list:
#     filtered_list = []
#     for elem in collection:
#         if filter_func(elem):
#             filtered_list.append(elem)
#     return filtered_list

def filter_words(w: str) -> bool:
    if type(w) != str:
        raise ValueError("dfgdg")
    return w.islower() and len(w) > 3

# print(my_filter(str.islower, words))
# print(my_filter(str.isupper, words))
# print(my_filter(str.isdigit, words))
# print(my_filter(filter_words, words))

# result = list(filter(str.islower, words))
# print(result)

# def is_even(num: int) -> bool:
#     return num % 2 == 0
#
# is_even = lambda num: num % 2 == 0

# print(lambda num: num % 2 == 0)


# result = filter(is_even, [1,2,3,4,5,6,7,8,9,10])
result = filter(lambda num: num % 2 == 0, [1,2,3,4,5,6,7,8,9,10])
print(list(result))
# tuple(result)



# def filter_upper_words(word: str):
#     return word.islower()
#
#
# # filter(filter_upper_words, ["hello", 'hi', "WORLD", "yes"])
# l = ["hello", 'hi', "WORLD", "yes"]
# filter_obj = filter(str.islower, l)
# print(type(filter_obj))
# print(list(filter_obj))
#
# # filtered = []
# # for elem in l:
# #     if str.lower(elem):
# #         filtered.append(elem)
# # return filtered
#
# print("".join(filter(lambda c: c not in "aAeEiIoOuU", "hello")))



# filter_obj = filter(str.islower, ["hello", 'hi', "WORLD", "yes"])
# print(set(filter_obj))




