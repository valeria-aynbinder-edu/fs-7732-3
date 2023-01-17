import json

# with open("data/json_example.json") as f:
#     content = f.read()
#     print(content)
#     print(type(content))
#
# print(content["members"])


# with open("data/json_example.json") as f:
#     content = json.load(f)
#     print(type(content))
#     print(content['members'])
#
# content['members'][0]['name'] = 'ttttttt'
#
# with open("data/json_example_new.json", "w") as f:
#     json.dump(content, f)

with open("data/list_json.json") as f:
    c = json.load(f)
    print(type(c))