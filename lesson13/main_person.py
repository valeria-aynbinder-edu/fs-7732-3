import datetime

from lesson12.person import Person, Student

if __name__ == '__main__':
    p1 = Person("Valeria", "Aynbinder", "NETANYA",
                "valeria@gmail.com", datetime.date(year=1987, month=2, day=11))
    # p2 = Person("Daniel", "Sh", "Ashdod",
    #             "daniel@gmail.com", datetime.date(year=2002, month=11, day=5))

    print(p1)
    print(type(p1))
    # print(p2)

    # persons_list = [p1, p2]
    # print(persons_list)

    s1 = Student("Daniel", "Sh", "Ashdod",
                 "daniel@gmail.com", datetime.date(year=2002, month=11, day=5))
    print(s1)
    print(type(s1))