
# functions
# motivating task:
# exersise - get a numbers from a user
# if the number can be divided by 2, but not by 3 or 5, print: "Nice".
# If the number can be divided by 2 and 3, but not by 5 print: "Good".
# if the number can be divided by 2,3 and 5, print: "Excellent".
# Otherwise print: "Ok".
# Every message you display to the user should be preceeded by
# the following pretty string:
# **********----------**********
# **********----------**********
# **********----------**********


# for example:


# **********----------**********
# **********----------**********
# **********----------**********

# Please insert a number

# **********----------**********
# **********----------**********
# **********----------**********

# 4

# **********----------**********
# **********----------**********
# **********----------**********

# Nice

def print_stars(stars_num):
    stars_str = f"{'*' * stars_num}-----------{'*' * stars_num}\n" * 3
    print(stars_str)

# print_stars(20)
# print_stars(2)
# print_stars(10)

# print_stars(7)
# num = int(input("Enter a number: "))
# stars = int(input("Enter stars num: "))
# print_stars(stars)
# if num % 2 == 0:
#     if num % 3 == 0:
#         if num % 5 == 0:
#             print("Excellent")
#         else:
#             print("Good")
#     else:
#         print("Nice")
# else:
#     print('OK')

# print_stars(stars)

# add parameter - allow user to choose amount of stars



import string
# print(string.ascii_lowercase)

def is_pangram(sentence):
    all_lower = string.ascii_lowercase
    sentence_lower = sentence.lower()
    for char in all_lower:
        if char not in sentence_lower:
            return False
    return True



# def my_sum(nums_list):
#     return sum(nums_list)
#
# my_sum([3,4,6,2])
# nums_list = [4,5,7]
# my_sum(nums_list)

##### INCORRECRT!!!!!!
# nums_list = [4,5,7]
# def my_sum():
#     return sum(nums_list)
#
#
# my_sum(nums_list)



# sentence = input("Insert your sentence: ")
# pangram = is_pangram(sentence)
# if pangram:
#     print("Your sentence is pangram")
# else:
#     print("Your sentence is not a pangram")

def get_sentence() -> str:
    return input("Insert your sentence: ")

pangram = is_pangram(get_sentence())
# 1, 3, 5, 7, 8, 10, 12
is_31_days_month()

year = int(input("Insert year: "))
is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# another task: given a month and a year, print number of days in that month

# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# if month != 2:
#     if (month <= 7 and month % 2 == 1) or (month > 7 and month % 2 == 0):
#         print("31 days")
#     else:
#         print("30 days")
# else:
#     if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
#         print("28 days")
#     else:
#         print("29 days")
#
# def is_leap_year(year):
#     return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
#
# def is_31_days_month(month):
#     return (month <= 7 and month % 2 == 1) or (month > 7 and month % 2 == 0)
#
# def days_in_month(month, year):
#     if month != 2:
#         if is_31_days_month(month):
#             return 31
#         else:
#             return 30
#         # return 31 if is_31_days_month(month) else 30
#     else:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#         # return 29 if is_leap_year(year) else 28

# scopes