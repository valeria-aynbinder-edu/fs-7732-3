import re



# user_email = input("Insert email: ")
#
# # letters (a-z) @ letters (a-z) . letters (a-z)
#
# pattern = "[a-z]+@[a-z]+\.[a-z]+"
# #
# result = re.match(pattern, user_email)
# #
# type(result)
# #
# print(result)

print(re.match("c", "cat"))
print(re.match("cat", "cat"))
print(re.match("cat", "ccat"))
print(re.match("c.", "cat"))
print(re.match("c[a-c]", "cat"))
print(re.match("c[a-c][A-Z]", "cat"))
print(re.match("c[a-c][A-Z]", "caT"))
print(re.match("[A-Z][a-z]", "cat"))
print(re.match("[A-Z][a-z]", "Cat"))
print(re.match("[A-Z][a-z]", "CAt"))
print(re.match("[A-Za-z]", "2At"))
print(re.match("[A-Za-z]", "apple"))


# quantity: * + ? {}
print(re.match("[A-Z][a-z]*", "Cat"))
print(re.match("[A-Z][a-z]*", "Ca"))
print(re.match("[A-Z][a-z]*", "C"))

print(re.match("[A-Z][a-z]+", "Cat"))
print(re.match("[A-Z][a-z]+", "Ca"))
print(re.match("[A-Z][a-z]+", "C"))


# a7b8c1
# aa
# a77
print(re.match("([a-c][0-9])+", "Cat"))
print(re.match("([a-c][0-9])+", "a7b8c1"))
print(re.match("([a-c][0-9])+", "aa"))
print(re.match("([a-c][0-9])+", "a1"))

print(re.match("([a-c][0-9])?", "a7b8c1"))
print(re.match("([a-c][0-9])?", "a"))
print(re.match("([a-c][0-9])?", "1"))

print(re.search("c", "search"))
print(re.match(".*[@#$%^&*]", "p@ssword"))
print(re.match(".*[@#$%^&*].*", "p@ssword"))
print(re.match(r"\\[tyuk]", "sdf\sdf"))
# C:\\sdfsdf\sdfs\sdf\file.txt
#
# s = '^[a-zA-Z]:\\(((?![<>:"\/\\|?*]).)+((?<![ .])\\)?)*$'
#
# #((?![<>:"\/\\|?*]).)+((?<![ .])\\)?
#
# # (?![<>:"\/\\|?*]).