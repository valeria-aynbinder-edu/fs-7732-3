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
max_num = nums[0]

for num in nums:
    if num > max_num:
        max_num = num
print(max_num)
