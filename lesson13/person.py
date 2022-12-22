# Base class / parent class
import datetime


class Person:
    def __init__(self, first_name: str, last_name: str, address: str, email: str, bdate: datetime.date):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address
        self.__email = email
        self.__birth_date: datetime.date = bdate

    def get_full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    def get_address(self):
        return self.__address

    def get_email(self):
        return self.__email

    def get_birth_date(self) -> datetime.date:
        return self.__birth_date

    def get_age(self):
        return datetime.date.today().year - self.__birth_date.year

    def __str__(self):
        return f"{self.get_full_name()}, lives at {self.get_address()}, {self.get_age()} years old"

    def __repr__(self):
        return self.__str__()

    # def __repr__(self):
    #     return self.get_full_name()

# Derived / child class
class Student(Person):

    def __str__(self):
        return f"Student: {super().__str__()}"
    # if no init - will inherit from the parent
    # def __init__(self, first_name: str, last_name: str,
    #              address: str, email: str, bdate: datetime.date, study_year):
    #     super().__init__(first_name, last_name, address, email, bdate)
    #
    #     self.study_year = study_year
    #     self.grades = []

    # def add_grade(self, grade):
    #     self.grades.append(grade)
    #
    # def get_best_grade(self):
    #     return max(self.grades)
    #
    # def __str__(self):
    #     return f"Student {super().__str__()}, starts studying at {self.study_year}"
#
#
# # Derived / child class
class Lecturer(Person):

    # if no init - will inherit from the parent
    def __init__(self, first_name: str, last_name: str, address: str, email: str,
                 bdate: datetime.date, salary_per_hour: int):
        super().__init__(first_name, last_name, address, email, bdate)
        # self.__salary = salary_per_hour
        self._salary = salary_per_hour

    def get_salary_per_hour(self):
        return self._salary

    def get_salary_per_course(self, course_hours):
        return self._salary * course_hours

    def __str__(self):
        return f"Lecturer {super().__str__()}"
#
#
class LeadLecturer(Lecturer):

    def __init__(self, first_name: str, last_name: str, address: str, email: str,
                 bdate: datetime.date, salary_per_hour: int, conference_salary_addition_percent: int):
        super().__init__(first_name, last_name, address, email, bdate, salary_per_hour)

        self.__conference_salary_addition_percent = conference_salary_addition_percent
        self.__conferences = []

    def add_conference(self, conference_name):
        self.__conferences.append(conference_name)

    def get_conferences_num(self):
        return len(self.__conferences)

    def get_salary_per_conference(self, conference_hours):
        return self._salary * (1+self.__conference_salary_addition_percent/100) * conference_hours
        # return self._salary * (1+self.__conference_salary_addition_percent/100) * conference_hours

    def get_salary_per_course(self, course_hours, bonus=0):
        return super().get_salary_per_course(course_hours) + bonus

    def __str__(self):
        return f"Lead {super().__str__()}"
