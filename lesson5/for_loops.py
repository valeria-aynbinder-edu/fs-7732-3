# i=0
# while i < 10:
#     print("********")
#     i += 1
#
# grades = [99, 98, 97, 80, 100, 75, 93]
# i = 0
# while i < len(grades):
#     print(grades[i])



# for iterating list
# for grade in grades:
#     print(grade)


# grades = [99, 98, 97, 80, 100, 75, 93]
# names = ['Herut', 'Lior', 'Chen', 'Gal']
# grades = []
# for name in names:
#     grade = int(input(f"Insert a grade for {name}"))
#     grades.append(grade)
# for i, name in enumerate(names):
#     print(f"Record number {i}: The grade of {name} is {grades[i]}")


# word = "Thursday"
# for char in word:
#     print(char)


# r = range(1_000_000)
# print(50_098 in r)
# print(r[5:15])
# for num in range(10):
#     print(num)

# for num in range(-5, 20, 3):
#     print(num)

# print(range(-5, 20, 3))

# my_range = range(-5, 0)
# print(my_range)

# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
#
# for i in range(len(cities)-1, -1, -1):
#     print(f"{countries[i]} - {cities[i]}")


# find max
nums = [54, -1, 45, 987, 5, 2, 65, 7, 12]
# max_num = nums[0]
#
# for num in nums:
#     if num > max_num:
#         max_num = num
# print(max_num)
#
# [1000, 54, -1, 45, 987, 5, 2, 65, 7, 12]
# [54, -1, 45, 987, 5, 100, 2, 165, 7, 12]

# nums = [-1, 54, 45, 987, 5, 2, 65, 7, 12]
# nums = [54, -1]
# [54, -1, 56] #Max = 56 secons = -1

# max = 54 second_max = -1
# num = 56
# max = 56
# [54, 5, 56]

#  * second_max  *  max  *

# max_num = max(nums[0:2])
# second_max = min(nums[0:2])
# max_num = nums[0]
# second_max = nums[1]
# for num in nums:
#     # if num < second_max:
#     #     continue
#     if second_max < num <max_num:
#         second_max = num
#     if num > max_num:
#         second_max = max_num
#         max_num = num


# while True:
#     num = input("Insert grades number: ")
#     if num.isdigit() and int(num) > 0:
#         num = int(num)
#         break
#
# names = []
# grades = []
# for i in range(num):
#     name = input("Insert name: ")
#     names.append(name)
#     while True:
#         grade = input(f"Insert {name}'s grade: ")
#         if grade.isdigit() and 0 <= int(grade) <= 100:
#             grade = int(grade)
#             grades.append(grade)
#             break
#
# print(f"Names: {names}, grades: {grades}")
# print(f"The avg is: {sum(grades)/num}")


# num = 19
#
# start_range = int(input("Insert start range: "))
# end_range = int(input("Insert end range: "))
# primes = []

# for num in range(start_range, end_range+1):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             # not prime
#             is_prime = False
#             break
#
#     if is_prime:
#         primes.append(num)
#
# print(primes)


rows = int(input("Num: "))
for i in range(1, rows+1):
    # print single row
    for j in range(1, i+1):
        print(j, end=" ")
    # print('')
    print('\n', end='')







