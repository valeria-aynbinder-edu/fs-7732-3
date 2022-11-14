# lists
# slicing operator
# nested lists
# my_list = []
# names = ['Tal', 'Daniel', 'Noam', 'Herut']
# grades = [98, 97, 100, 99]
# print(names)
# print(grades)
# print(type(names))
# student_num = 2
# print(names[student_num], grades[student_num])

# num = int(input("Insert student num"))
# print(names[num], grades[num])

# get student grade by name
# name = input("Insert student name: ").title()
# if name not in names:
#     print("The name does not exist")
# else:
#     idx = names.index(name)
#     print(f"The grade of {name} is: {grades[idx]}")

# slicing
# names = ['Tal', 'Daniel', 'Noam', 'Herut']
# grades = [98, 97, 100, 99]
#
# new_list = names[:2]
# new_list = names[::-2]
# new_list = names[0:1]
# # print(new_list)
# new_list = names[0]
# new_list = names[0:2:-1]
# print(names[0][0:2:-1])
# tal = names[0]
# print(tal)
# print(names[0][2:3])
# names[0]: 'Tal'
# print(new_list)

# methods that do not return values,
# but change the list itself
# names1 = ['Lior', 'Chen', 'Gal']
# print(names)
# names.extend(names1)
# print(names)
# names.append("Raul")
# print("after append", names)
# names.sort()
# print("after sort", names)
# names.sort(reverse=True)
# print("after sort", names)
# names.reverse()

# my_list = ["apple",
#            5,
#            True,
#            "ananas",
#            6.4,
#            [10,
#             20,
#             30,
#             ["a", "b", "c"]]]
# print(my_list)
# print(my_list[0])
# print(my_list[-1])
# print(type(my_list[-1]), my_list[-1])
# print(my_list[-1][-1][-1])

# countries = ["Israel", "UK", "Ukraine", "US"]
# cities = [["Tel Aviv", "Haifa", "Yerucham", "Petah Tikva"],
#           ["London", "Manchester"],
#           ["Kyiv", "Cherson"],
#           ["New York", "Los Angeles", "Las Vegas"]]
# country = input("Insert country: ")
# city = input("Insert city: ").title()
# if country in countries:
#     idx = countries.index(country)
#     if city in cities[idx]:
#         print("You are right!")
#     else:
#         print(f"{city} is not in {country}")
# else:
#     print("Country is not in our DB")


# list1 = [1, [10, 20, [100, [[10_000, 20_000, 30_000], 2000, 3000], 300]]]
# 10
# print(list1[1][0])
# 20000
# print(list1[1][2][1][0][1])

# [2000, 3000]
# print(list1[1][2][1][1:])

# lists slicing exercise

# fruits = ['banana', 'apple', 'mangustin']
# vegs = ['tomato', 'cucumber', 'onion']
# fruits.extend(vegs)
# # fruits.append(vegs)
# print(fruits)
# fruits_and_veg = fruits
# print(fruits_and_veg)


# list methods

# lists slicing - exercise

# while loops
# count = 0
# grades = []
# while count < 3:
#     grade = int(input("grade: "))
#     grades.append(grade)
#     count += 1
# print(grades)

# num = input("Insert a num: ")
# while not num.isdigit():
#     num = input("Please try again: ")
# print("Great!")

# incorrect_input = True
# first_iteration = True
# message = "Insert a num: "
#
# while incorrect_input:
#
#     if not first_iteration:
#         message = "Please retry: "
#
#     num = input(message)
#     if num.isdigit():
#         incorrect_input = False
#     first_iteration
#
# print("Great")

# option 2

# incorrect_input = True
# message = "Insert a num: "
#
# while incorrect_input:
#
#     num = input(message)
#     if num.isdigit():
#         incorrect_input = False
#
#     message = "Please retry: "
#
# print("Great")

# while True:
#     num = input("Insert a num: ")
#     if num.isdigit():
#         break
#     print("After if")
#
# print("Great")
# print("Bye-bye")

# while True:
#     num = input("Insert a num or $ to finish: ")
#     if num == '$':
#         break
#     num = int(num)
#     if num % 10 == 0:
#         continue
#     print(num)



# iterate x times
# iterate unknown amount of times
# break
# continue
# pass


# Write a program that gets numbers from a user until the user inserts $
# After the user inserts $, print the sum of the numbers and the average



# iterate list using while
grades = [95, 98, 87, 65, 100, 77, 99]
n = input("sdfsdfs: ")
i = 0
while i < len(grades):
    if grades[i] >= 95:
        print(grades[i])
    i += 1



# debugging?