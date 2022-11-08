######
# Modulus - getting length of the movie in minutes
# and printing the length in format hh:mm
######
# num = int(input("Insert minutes:"))
# hours = num // 60
# minutes = num % 60
# print(hours, ":", minutes)
# print(f"The length of the movie is: {hours}:{minutes}")
# print("The length of the movie is: {hours}:{minutes}")


######
# Modulus - getting length of the movie in seconds
# and printing the length in format hh:mm
######
#
# total_seconds = int(input("Insert seconds:"))
#
# # total whole hours
# hours = total_seconds // 3600
#
# # calculating remaining seconds
# # seconds_in_whole_hours = hours * 3600
# # seconds_remainder = total_seconds - seconds_in_whole_hours
# seconds_remainder = total_seconds - hours * 3600
#
# # calculating remaining minutes and seconds
# minutes = seconds_remainder // 60
# seconds = seconds_remainder % 60
#
# #print the result
# print(f"{hours}:{minutes}:{seconds}")

########
# boolean
# comparison operators
# logical operators - and / or
########

# my_bool = True
# my_bool = False
# print(type(my_bool))
#
# salary = int(input("Insert your salary"))
# is_minimum_salary = salary < 5000
# print("Is your salary smaller than minimum:",
#       is_minimum_salary)

# salary == 7000
# salary = 7000
# 6 < 8
# 6 > 8
# 6 >= 8
# 6 <= 8
# 6 == 8
# 6 != 8

# True and True
# False and False
# True and False
# False and True

#
#
# True or True
# True or False
# False or True
# False or False


#####
# exercise - print whether user can drive
#####

# beer 0.3 or less
# wine 0.2 or less

# drink = input("Insert your drink") # beer / wine
# qty = float(input("Insert qty"))
# can_drive = (drink == 'beer' and qty <= 0.3) \
#             or (drink == 'wine' and qty <= 0.2)
#
# print("Can drive: ", can_drive)


# day = int(input("Insert day: "))
# month = int(input("Insert month: "))
# is_winter = month == 12 or month == 1 or month == 2
# is_spring = 3 <= month <= 5


#####
# conditional statements - if / else
#####

# money = int(input("Your money: "))
# if money == 1000000:
#     print("You are a milioner")
# elif money >= 10 ** 7:
#     print("You are a billion")
# elif money > 1000000:
#     print("You are a multi-milioner")
# else:
#     print("You are not a milioner")
# print("Bye")
#
# money = int(input("Your money: "))
# if money == 1000000:
#     print("You are a milioner")
# elif 1_000_000 < money <= 10 ** 7:
#     print("You are a multi-milioner")
# elif money > 10000000:
#     print("You are a bilioner")
# else:
#     print("You are not a milioner")
# print("Bye")



########
# The difference between if and elif
########

# num = int(input("Insert a num: "))
# if num < 10:
#     print("AAA")
# elif num < 20:
#     print("BBB")
# print("CCC")
#
#
# num = int(input("Insert a num: "))
# if num < 10:
#     print("AAA")
# if num < 20:
#     print("BBB")
# print("CCC")
#
# num = int(input("Insert a num: "))
# if num < 10:
#     print("AAA")
# else:
#     print("BBB")
# print("CCC")
#
#
# drink = input("drink type")
# qty = float(input("qty"))
# if drink == 'beer' and qty <= 0.3:
#     print("you can drive")
# elif drink == 'wine' and qty <= 0.2:
#     print("you can drive")
# else:
#     print("you cannot drive")

#######
# NESTED IFs
########

# qty = float(input("qty: "))
# drink_type = input('drink type: ')
# if drink_type == 'beer':
#     beer_type = input("Insert beer type") #strong / regular
#
# can_drive = None
#
# if drink_type == 'beer':
#     if beer_type == 'strong' and qty <= 0.25:
#         can_drive = True
#     elif beer_type == 'regular' and qty <= 0.3:
#         can_drive = True
# elif drink_type == 'wine' and qty <=0.2:
#     can_drive = True
#
# if can_drive:
#     print("You can drive")

#######
# Rock scissors paper (not completed - complete by yourself!)
########

# player1 = input("Player 1: ")
# player2 = input("Player 2: ")
#
# if player1 == player2:
#     print("Draw")
# elif player1 == "scissors":
#     if player2 == 'rock':
#         print("2 wins")
#     else:
#         print("1 wins")
# elif player1 == "paper":


#####
# string slicing
#####
text = "Hello world"

# print(text[:6])
# print(text[2:10:2])
# print(text[2:10:-2])
# print(text[10:2:-2])
# print(text[::-1])
#print(text[-1])
# print(text[-6:-2:1])
print(text[-2:-6:1])


