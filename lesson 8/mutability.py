

# mutability
# num1 = 35
# num2 = 45
# print(id(num1), id(num2))
# my_list = [num1, num2]
# print("my_list[0]", id(my_list[0]))
# print(id(my_list))
# print(my_list)
# num1 = 50
# print(id(my_list))
# print(my_list)
# print("my_list[0]", id(my_list[0]))
# my_list[0] = 800
# print("after my_list[0] = 800")
# print("my_list[0]", id(my_list[0]))
# l1 = [35]
# l2 = [45]
# my_list = [l1, l2]
# print(my_list)
# l1[0] = 50
# print(my_list)

# my_list = [1, 2]
# print("id(my_list[0])", id(my_list[0]))
# print("id(my_list[1])", id(my_list[1]))
# my_list.insert(1, 3)
# print("id(my_list[0])", id(my_list[0]))
# print("id(my_list[1])", id(my_list[1]))
# print("id(my_list[2])", id(my_list[2]))
# print(my_list[0] is my_list[1])
# print(id(my_list[0]) == id(my_list[1]))

# name1 = input("insert name1: ")
# name2 = input("insert name2: ")
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = "aaa"
# name2 = "aaa"
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = 111
# name2 = 111
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)

# name1 = int(input("insert num"))
# name2 = int(input("insert num"))
# print("name1 == name2", name1 == name2)
# print("name1 is name2", name1 is name2)


# num1 = 50
# print(id(num1))
# num1 = 55
# print(id(num1))

# vs
# l1 = []
# print(id(l1))
# l1.append(5)
# print(id(l1))
# # vs
# l1 = [5]
# print(id(l1))


# num2 = 60
# print(id(num2))
# num2 = num1
# print(id(num2))
# x = input("text:  ")
# y = input("text:  ")
# x = "apple"
# y = "apple"
# x = []
# y = []
# print(x == y)
# print(x is y)
# print(id(x), id(y))

# l = [['Paris', 'London', 'New York'],
#      [45, True, 5.5, 'hello'], -3,
#      [5, ['#', '$', '%', '^', [10, 20, 30, 40]]],
#      [['a'], ['b'], 'c', [['d']]]]
# cities = l[0]
# numbers = l[3][1][4]
# numbers = l[3][1][4] = "www"
# l[3][1][4] = "www"
# cities = "World"
# cities[0] = "Tel Aviv"
# print(l)
# print(numbers)

# s = "Paris"
# s_lower = s.lower()
# print(s is s_lower)

# names = []
# grades = []
# for name_idx in range(3):
#     grades.append([])
#     names.append(input("Insert a name"))
#     for grade_idx in range(2):
#         grades[name_idx].append(int(input("insert grade: ")))
# print(names, grades)

# names = ['VAleria', 'Shay', 'Ziv']
# names1 = names.copy()
# names2 = names
# print(names is names2)
# print(names is names1)

# names = [["Shay", "Ziv"],
#          ["Nehorai"],
#          ["Noa", "Tamar"]]
# names1 = names.copy()
# names[0][0] = "Valeria"
# names1[0][0] = "VVVVVV"
# print(names1)
# print(names)
# print(names is names1)

# import copy
# copy.deepcopy(names)