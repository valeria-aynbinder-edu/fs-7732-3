# mutability
# name1 = input("Insert a name: ")
# name2 = input("Insert a name: ")
# print(f"id of name1: {id(name1)}")
# print(f"id of name2: {id(name2)}")
# print("name1 is name2", name1 is name2)
# print("name1 == name2", name1 == name2)
# name3 = name1
# print("name1 is name3", name1 is name3)
# print("name1 == name3", name1 == name3)

# d1 = {1: 'a', 2: [2, 3, 'dfg']}
# d2 = {3: 'c', 4: 'd', 5: 'e'}
# d3 = {1: 'a', 2: [2, 3, 'dfg']}
# print(d1 == d3)


grades = {
    'noam': {
        'python': [99, 100],
        'sql': [98, 90]
    },
    'joshua': {
        'python': [98, 100, 97],
        'sql': (99, 99)
    }
}
# noam_sql = grades['noam']['sql']
# grades['noam']['sql'].append(100)
# print(noam_sql)
# print(noam_sql is grades['noam']['sql'])

# joshua_sql = grades['joshua']['sql']
# grades['joshua']['sql'] = (99, 99, 100)
# print("joshua_sql", joshua_sql)
# print("grades['joshua']['sql']:", grades['joshua']['sql'])

# #DR
# def foo(word: str):
#     word = 'Dr' + word
#     return word
#
# a = 'Omer'
# result = foo(a)
# print(a)
#
# def foo(word: list):
#     word.insert(0, 'D')
#     word.insert(1, 'r')
#     word.insert(2, ' ')
#     # return word
#
# a = ['O', 'm', 'e', 'r']
# foo(a)
# print(a)
# # print(result is a)


# def foo(word: list):
#     print(id(word))
#     word = ['r', 't']
#     return word
#
# a = ['O', 'm', 'e', 'r']
# print(id(a))
# result = foo(a)
# print(a)
# print(result)
# print(result is a)

# implement a function that receives
# a list of strings and returns a list
# that contains all the strings with
# uppercase
# def foo1(words: list) -> list:
#     ret_list = []
#     for elem in words:
#         ret_list.append(elem.upper())
#     return ret_list
#
# def foo2(words: list) -> list:
#     for i in range(len(words)):
#         words[i] = words[i].upper()
#     return words
#
# my_list = ['valeria', 'gal', 'chen']
# new_list = foo2(my_list)
# print(my_list, new_list)

# nums = [3, 4, 5, 8, 2, 3]
# nums.sort()
# ret_val = nums.sort()
# ret_val = sorted(nums)
# print(nums, ret_val)

fruits = [['apple', 'pear'],
          ['banana', 'mango'],
          ['orange', 'clementina']]

# new_list = []
# for i in fruits:
#     new_list.append(i)
#
# new_list[0][0] = 'mangustin'
# fruits[0][0] = 'mangustin'
#
# print(fruits)
# print(new_list)

# new_list[0] = ['mangustin', 'salak']
# print(fruits)
# print(new_list)

fruits = [['apple', 'pear'],
          ['banana', 'mango'],
          ['orange', 'clementina']]

# new_fruits = fruits
#
# new_fruits = []
# for elem in fruits:
#     new_fruits.append(elem)
#
# new_fruits = fruits
# fruits[0] = []
# fruits[1][0] = 'bla'
# print(fruits)
# print(new_fruits)

# vegs = ['tomato', 'cuecumber', 'potato']
# # new_vegs = vegs
# new_vegs = vegs.copy()
# vegs[0] = 'onion'
# print(vegs)
# print(new_vegs)

# new_fruits = fruits.copy()
# fruits[0] = []
# print(fruits)
# print(new_fruits)
# fruits[1][0] = 'tomato'
# print(fruits)
# print(new_fruits)


board = """
      1   2   3
    - - - - - - - 
 1  | x |   |   |
    -------------
 2  |   | x |   |
    -------------
 3  |   |   | 0 |
    -------------
"""
print(board)
input("INsert: ")
board = """
      1   2   3
    - - - - - - - 
 1  | x | 0 |   |
    -------------
 2  |   | x |   |
    -------------
 3  |   |   | 0 |
    -------------
"""
print(board)

board = [['x', 'o', None],
         ['o', 'x', 'x'],
         ['o', 'o', None]]


# get board size
# get players name
# draw a board
# while True:
#     pass
    # ask for turn of player
    # redraw board with turn
    # check wins
        # rows
        # columns
        # diagonal


def check_row_wins(board: list[list]) -> str | None:
    board_size = len(board)
    for row in board:
        if row.count('x') == board_size:
            return 'x'
        elif row.count('o') == board_size:
            return 'o'
        else:
            return None





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