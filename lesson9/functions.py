# optional arguments
# create_person

# def my_sum(p1, p2):
#     pass
#
# my_sum(4)
#
# def create_person(peron_id, name, address, middle_name='der'):
#     return {
#         'id': peron_id,
#         'name': name,
#         'address': address,
#         'middle_name': middle_name
#     }
# print(create_person('a','b','c'))
# print(create_person(peron_id='a',name='b',address='y', middle_name='c'))
# print(create_person(name='b',address='y',peron_id='a', middle_name='c'))
# print(create_person(peron_id='a',name='b','y', 'c'))

# def calc_bmi(weight, height, age):
#     pass
#
# calc_bmi(weight=56,
#          height=160,
#          age=30)
#
# calc_bmi(56, age=30, weight=160)

# print("Hello", "sdfsdf", "4", "Sdf")

a, b = (4,5)
head, *tail = (4,5,6,7)

# *args
def a(*args):
    print(f"type of args: {type(args)}, len: {len(args)}")
    for arg in args:
        print(arg)
a(3, 4, 5, 7, 8)

# *head, tail = 6,7,8
#
# def aa(*args, param1):
#     print(f"type of args: {type(args)}, len: {len(args)}")
#     for arg in args:
#         print(arg)
# aa(5)

# def b():
#     pass
#
# b(6)

# **kwargs

# a('Hello', 'Welcome', 'to', 'Python', 'Class')

# def aa(argv:tuple):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)
#
# aa(('Hello', 'Welcome', 'to', 'Python', 'Class'))
# a()

# def a1(argv):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)

#a1(4,5)
#
# def b(person_id, name, *phone_numbers):
#     print ("First argument :", person_id)
#     print ("Second argument :", name)
#     for arg in phone_numbers:
#         print("Next argument through *phone_numbers :", arg)
#
# b(234, 'Valeria', '045-w4564', '045-srdfg', '0456456-dfg')

# b()

def create_person(person_id, name, address, **kwargs):
    print(person_id, name, address)
    print(type(kwargs))
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

create_person(123, 'valeria', 'netanya',
              height=160,
              age=35,
              phone='054-48754987')

# def cc(person_id, name, **kwargs):
#     print(person_id, name)
#     print(kwargs)
#
# c(first='Python', mid ='Full', last='Stack')
# cc(345345, 'Valeria', work_address="tel aviv", age=40)
# c()
# c("Pyton")

# [3,4,1,2,6].sort(reverse=True)


def d(arg1, **kwargs):
    print(f"arg1: {arg1}")
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")
#
# d(5, first="Hello", second="Bye")
# d(first=3)
# d(5, 'Hello')

#
#

# head, *tail = (1, 2,3,4)
#
def d(person_id, name, *args, **kwargs):
    print(person_id)
    print(name)
    print(f"args num: {len(args)}, args: {args}")
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")
#
#d(person_id=5345, name='ziv', 'trrr', 56, first='abc', second='def')
# d()
# d(first='abc', 5)

# **kwargs

l1 = [1,2,3]
l2 = [10, 20, 30]
for elem1, elem2 in zip(l1, l2):
    pass
