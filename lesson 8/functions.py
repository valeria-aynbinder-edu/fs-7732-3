# optional arguments
# create_person

# *args
# def a(*argv):
#     print(f"type of argv: {type(argv)}, len: {len(argv)}")
#     for arg in argv:
#         print (arg)

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

def c(**kwargs):
    print(type(kwargs))
    print(kwargs['first'])
    print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")

def cc(person_id, name, **kwargs):
    print(person_id, name)
    print(kwargs)
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
# def d(person_id, name, *args, **kwargs):
#     print(person_id)
#     print(name)
#     print(f"args num: {len(args)}, args: {args}")
#     print(f"kwargs num: {len(kwargs)}, kwargs: {kwargs}")
# #
# d(5345, 'ziv', 'trrr', 56, first='abc', second='def')
# d()
# d(first='abc', 5)

# **kwargs