# nums = [7, 8, 43, 5, 2, 7, 2, 6]
# print(nums[2:5])
# print(nums[2:])
# print(nums[:5])
# print(nums[:5:2])
# print(nums[3])
# print(nums[3:4])
#
# word = "banana and apple"
# print(word[::-1])


# a = 5
# b = 6
# if a != b:
#     print('bla')
# if a is not b:
#     print('bla')
#
# s = "dfsdf"
# if s is None:
#     pass

# ['banana','apple','pear']
# a 2
# p 2
# e 1

# a = 5
# b = 5
# print(a is b)
# c = input("insert num1:")
# d = input("insert num2:")
# print(c is d)




d= {'Science': [88, 89, 62, 95],
'Language': [77, 78, 84, 80]}

#[{'Science': 88, 'Language': 77},
# {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84},
# {'Science': 95, 'Language': 80}]

def dict2list(orig_dict) -> list:
    ret_list = []
    for prof, grades_list in orig_dict.items():
        for i, grade in enumerate(grades_list):
            if len(ret_list) < i+1:
                ret_list.append({})
            ret_list[i][prof] = grade
    return ret_list

print(dict2list(d))

# []
# [{}] -> [{'science': 92}]
# [{'science': 92}, {'science': 90},
#  {'science': 99}, {'science': 99}]
# [{'science': 92, 'lang':70}, {'science': 90, 'lang': 70},
#  {'science': 99, 'lang':70}, {'science': 99, 'lang':70}]