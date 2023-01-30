# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the
# iterator protocol, which consist of the methods iter() and next().
# Lists, tuples, dictionaries, and sets are all iterable objects.
# They are iterable containers which you can get an iterator from.
# All these objects have a iter() method which is used to get an iterator:

# __iter__
# __next__
#
# iter()
# next()
#
my_list = [1,2,3,4]
# for i in my_list:
#     print(i)

# __iter__
# __next__

# list_iter = iter(my_list)
# print(type(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))

class MyNumbers:

    def __init__(self, start=0, end=10):
        self.start_from = start
        self.end = end

    def __iter__(self):
        self.counter = self.start_from
        return self

    def __next__(self):
        if self.counter > self.end:
            raise StopIteration()
        curr = self.counter
        self.counter += 1
        return curr

# my_nums = iter(MyNumbers(5, 7))
# next(my_nums) # 5
# next(my_nums) # 6
# next(my_nums) # 7
# next(my_nums) # 6

for i in MyNumbers(5, 7):
    print(i)

#
#
# myclass = MyNumbers()
# myiter = iter(myclass)
#
# for i in myiter:
#     print(i)

class MyNumbers:
    def __init__(self, max_limit):
        self.max_limit = max_limit

    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        if self.a <= self.max_limit:
            self.a += 1
            return self.a
        else:
            raise StopIteration


myclass = MyNumbers(10)

# for x in myclass:
#     print(x)