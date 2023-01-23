# # sorted([3, 1, -5, 6, 9])
# # sorted([3, 1, -5, 6, 9], reverse=True)
# import datetime
#
# students = [
#     {"name": "Moshe", "grade": 89},
#     {"name": "David", "grade": 93},
#     {"name": "Jack", "grade": 73},
# ]
# # print(list(sorted(students)))
#
#
# # l = [2, 4, -1, 5]
# # sorted_list = []
# # for i in range(len(l), -1, -1):
# #     # find min
# #     # m = min(l)
# #     m = l[0]
# #     for j in l:
# #         if j < m:
# #             m = j
# #     sorted_list.append(m)
#
#
#
# def my_key_func(student):
#     return student["grade"]
#
# students = [
#     {"name": "Moshe", "grade": 89},
#     {"name": "David", "grade": 93},
#     {"name": "Jack", "grade": 73},
# ]
#
# # print(sorted(set([3,4,65, 3,4])))
# print(sorted(students, key=lambda s: s['grade'], reverse=True))
# #
# # sorted(students, key=my_key_func, reverse=True)
#
#
# class Vehicle:
#     def __init__(self, model, km):
#         self._model = model
#         self._km = km
#
#     def get_km(self):
#         return self._km
#
#     def __repr__(self):
#         return f"{self._model}, {self._km}"
#
#     # def __cmp__(self, other):
#     #     if self._km < other._km:
#     #         return -1
#     #     elif self._km == other._km:
#     #         return 0
#     #     else:
#     #         return 1
#     #
#     # def __gt__(self, other):
#     #     return self._km > other._km
#     #
#     # def __lt__(self, other):
#     #     return self._km < other._km
#
# vehicles = [Vehicle('mazda', 1000),
#             Vehicle('toyota', 50),
#             Vehicle('mercedes', 30000)]
#
#
# print(sorted(vehicles, key=lambda v: v.get_km()))
# print(sorted(vehicles, key=lambda v: v._model, reverse=True))
#
# # List elements: (Student's Name, Grade, Age)
# # sort first by highest grade, then smallest age
#
# participant_list = [
#     ('Alison', 50, 18), #4
#     ('Terence', 75, 12), #2
#     ('David', 75, 20), #3
#     ('Jimmy', 90, 22), #1
#     ('John', 45, 12) #5
# ]
#
# (50, 18)
# (25, 12)
# (25, 20)
#
# print(sorted(participant_list,
#        key=lambda x: (x[1], x[2])))
#
# # comparing tuples
# print((3, 2) > (1, 4))
# print((3, 2) > (3, 4))
# print((3, 2, 1) > (3, 2, 0))
# print((3, 2, 0) > (3, 2))
# # "apple" < "amazon"
#
# # def multi_key_func(participant):
# #     return 100 - participant[1], participant[2]
# #
# # sorted(participant_list, key=multi_key_func)
#
# words = ["sdfdf", "wdda", "re", "sdfgnjfjfku"]
# sorted(words, key=len)
#
# sorted(words, key=lambda w: len(w))
#
# my_compare = lambda w: len(w)
# sorted(words, key=my_compare)
#
# def my_best_compare(w):
#     return len(w)
# sorted(words, key=my_best_compare)
import datetime

d1 = "1h 5m"
tr1: datetime.timedelta = datetime.datetime.strptime(d1, "%Hh %Mm") - \
      datetime.datetime(year=1900, month=1, day=1)
print(tr1.total_seconds() // 60)

