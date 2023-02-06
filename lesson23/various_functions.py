import math

from lesson23.decorators import greeting_decorator

def my_dec(other_func):
    return 5

@greeting_decorator
def factorial():
    num = int(input("Please insert a number: "))
    fact = math.factorial(num)
    print(f"The factorial of {num} is {fact}")
#
# factorial = greeting_decorator(factorial)


def capitalize():
    txt = input("Please insert a text to capitalize: ")
    print(f"Your capitalized text is: {txt.capitalize()}")

# capitalize = my_dec(capitalize)

def convert_from_farenheit():
    temp_F = float(input("Please insert a temperature in °F: "))
    temp_C = (temp_F - 32) * (5/9)
    print(f"{temp_F} in °F is {temp_C} °C")


@greeting_decorator
def convert_from_celcius():
    temp_C = float(input("Please insert a temperature in °C: "))
    temp_F = (temp_C * (9/5)) + 32
    print(f"{temp_C} in °C is {temp_F} °F")

@greeting_decorator
def get_sum(n1, n2):
    return n1 + n2

# get_sum = greeting_decorator(get_sum)
# get_sum = greeting_decorator(get_sum)


if __name__ == '__main__':
    result = get_sum(10, 20)
    factorial()
    # convert_from_celcius()
    # greeting_decorator(convert_from_farenheit)()
    # capitalize()