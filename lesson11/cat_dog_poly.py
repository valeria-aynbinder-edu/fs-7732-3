class Cat:
    def __init__(self, cat_type, color, name):
        self.cat_type = cat_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, dog_type, color, name):
        self.dog_type = dog_type
        self.color = color
        self.name = name

    def make_sound(self):
        print("Wof")


cat = Cat('russian blue', 'grey-blue', 'Oliver')
dog = Dog('doberman', 'black', 'Bruno')

# cat.make_sound()
# dog.make_sound()
#
# # print(cat.name, dog.name)
#
# animals_list = [cat, dog]
# for animal in animals_list:
#     print(animal.name)
#     animal.make_sound()

#
# 5 + 8
# 5 + 0.9
# "apple" + "banana"

l1 = [2, 3,45,7]
word = "hello"

len(l1)
len(word)











