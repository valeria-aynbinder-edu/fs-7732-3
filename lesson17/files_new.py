relative_path = "../lesson18/data/alice_in_wonderland.txt"
absolute_path = "/lesson18/data/alice_in_wonderland.txt"

file_descriptor = open(relative_path, 'r')
# print(type(file_descriptor))
content = file_descriptor.read(1000)
content = file_descriptor.read(500)
file_descriptor.seek(0)
content = file_descriptor.read(500)
print(len(content))
print(content)
file_descriptor.close()