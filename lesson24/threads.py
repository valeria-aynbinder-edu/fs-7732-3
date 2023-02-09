from threading import Thread


def do1():
    print("1")

def do2():
    print("2")

def do3():
    print("3")

if __name__ == '__main__':
    # do1()
    # do2()
    # do3()
    print("Hello")
    thread = Thread()