# with open('my_text.txt', 'w') as fh:
#     fh.write("The sun is shining!\n")

# with open('my_text.txt', 'w') as fh:
#     fh.write("Hello!\n")

# with open('my_text.txt', 'a') as fh:
#     fh.write("SUN!\n")

with open("numbers.txt", "w") as f:
    for i in range(1, 11):
        f.write(str(i)+"\n")

numbers_list = [f"{i}\n" for i in range(1, 11)]
with open("numbers1.txt", "w") as f:
    f.writelines(numbers_list)

# with open('data/new_text.txt', 'a') as fh:
#     fh.write("SUN!\n")

# with open("/Users/valeria/Downloads/view_for_post.jpeg", 'rb') as fh:
#     content = fh.read()
#     print(type(content))
#     print(content[:100])
#     print("done")