# student = {
#     'name': 'David',
#     'city': 'Tel Aviv',
#     'grades': {'math':[98, 87, 90],
#                'english': [85]
#                }
# }
#
# import json
#
# dict_as_str = json.dumps(student)
# print(type(dict_as_str))
# print(dict_as_str)
#
# with open('student.json', 'w') as fh:
#     json.dump(student, fh)
#
# with open('student.json', 'r') as fh:
#     reloaded_student = json.load(fh)
#
# reloaded_student[0]['grades']['math'][2]



import json

dict1 = {}

# with open('data/example_2.json') as fh:
#     ret_val = json.load(fh)
# print(type(ret_val))
# print(ret_val)
# print(len(ret_val))
# print(ret_val['quiz']['sport'])

# with open('data/example.json') as fh:
#     my_dict = fh.read()

with open('data/json_example..json') as fh:
    ret_val = json.load(fh)

print(len(ret_val['challenges']))

# print(type(my_dict))
# print(my_dict)
# # my_dict['quiz']


# with open('data/person.json') as fh:
#     ret_val = json.load(fh)
# print(type(ret_val))
# print(ret_val)






