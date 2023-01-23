def filter_upper_words(word: str):
    return word.islower()


# filter(filter_upper_words, ["hello", 'hi', "WORLD", "yes"])
l = ["hello", 'hi', "WORLD", "yes"]
filter_obj = filter(str.islower, l)
print(type(filter_obj))
print(list(filter_obj))

# filtered = []
# for elem in l:
#     if str.lower(elem):
#         filtered.append(elem)
# return filtered

print("".join(filter(lambda c: c not in "aAeEiIoOuU", "hello")))



# filter_obj = filter(str.islower, ["hello", 'hi', "WORLD", "yes"])
# print(set(filter_obj))


