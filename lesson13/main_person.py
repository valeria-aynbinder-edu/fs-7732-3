import datetime

from lesson13.person import Person, Student, Lecturer, LeadLecturer

if __name__ == '__main__':
    # p1 = Person("Valeria", "Aynbinder", "NETANYA",
    #             "valeria@gmail.com", datetime.date(year=1987, month=2, day=11))
    # p2 = Person("Daniel", "Sh", "Ashdod",
    #             "daniel@gmail.com", datetime.date(year=2002, month=11, day=5))

    # print(p1)
    # print(p2)



    s1 = Student("Daniel", "Sh", "Ashdod",
                 "daniel@gmail.com", datetime.date(year=2002, month=11, day=5),
                 "python full stack")
    s1.add_grade(100)
    s1.add_grade(99)
    print(s1.get_avg_grade())

    # print(s1)

    # print(s1)
    # persons_list = [p1, s1]
    # print(persons_list)

    s2 = Student("Gal", "Mesilati", "Herzliya", "gal@gmail.com",
                 datetime.date(year=2000, month=3, day=28), "python full stack")
    print(s2.get_full_name())
    l1 = LeadLecturer("Valeria", "Aynbinder", "NETANYA",
                  "valeria@gmail.com", datetime.date(year=1987, month=2, day=11),
                      10, 15)
    print(l1)










