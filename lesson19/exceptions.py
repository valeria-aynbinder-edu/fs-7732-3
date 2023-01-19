import datetime


# return values vs raising exceptions
# what do we return if there is a problem?
# birth_year is negative, age is negative?

class NegativeYearError(Exception):
    pass


# class YearInFutureError(Exception):
#      def __init__(self, msg):
#          super().__init__(msg)

# class Exception:
#     def __init__(self, msg):
#         self.msg = msg
#
#     def __str__(self):
#         return self.msg

class YearInFutureError(Exception):
    def __init__(self, inserted_year):
        super().__init__(f"You inserted year {inserted_year} which is in the future")



# raise YearInFutureError()

def get_age(birth_year: int) -> int:
    if birth_year < 0:
        # raise Exception("Negative year is not allowed")
        raise NegativeYearError()
    if birth_year > datetime.datetime.utcnow().year:
        raise YearInFutureError(birth_year)
    return datetime.datetime.utcnow().year - birth_year



try:
    b_year = int(input("Insert your year: "))
    age = get_age(b_year)
    print(f"You are {age} years old")
    print("Inside try after get_age")
except ValueError:
    print("You did not insert a number")
except NegativeYearError:
    print("Negative year")
except Exception as e:
    print(e)
finally:
    print("Inside finally")
# except Exception as e:
#     print(e)
print("bye")


try:
    fd = open("my_file", "r")
    content = fd.read()
    get_age()

except:
    pass
finally:
    fd.close()

# num = int(input("Insert num"))

# exceptions you've already seen


# num = int(input("Insert your birth year: "))
# age = datetime.datetime.utcnow().year - num
# print(f"You are {age} years old")


# try:
#     num = int(input("Insert your birth year: "))
#     age = datetime.datetime.utcnow().year - num
#     print(f"You are {age} years old")
# except:
#     print("You did not insert a number")


# while True:
#     try:
#         num = int(input("Insert your birth year: "))
#         age = datetime.datetime.utcnow().year - num
#         print(f"You are {age} years old")
#         break
#     except:
#         print("You did not insert a number")


# we can differentiate between error types!

# def divide_dictionary_values(dictionary, keys):
#     try:
#         key1 = keys[0]
#         key2 = keys[1]
#         print(dictionary[key1] / dictionary[key2])
#     except KeyError as error:
#         print(f"Provided key does not exist in the dictionary: {error}")
#     except ZeroDivisionError as zde:
#         print(f"You tried to divide by zero")
#     except TypeError as val_err:
#         print("TypeError")
#     except Exception as unknown_exc:
#         print(f"Unknown error of type {type(unknown_exc)}: {unknown_exc}")


# Create your own Exception
# Exceptions are Objects that inherit from Exception

# class MyException(Exception):
#     pass

# exception propagates until someone catches it

# finally

# adding exceptions to Table System