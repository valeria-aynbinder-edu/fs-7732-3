import threading

def a_lot_of_calc(num:int):
    print(f"started a_lot_of_calc with {num}")
    s = 0
    for i in range(10000):
        s += num ** i
    print(f"finished a_lot_of_calc {s}")

if __name__ == '__main__':

    print("hello")
    num = int(input("Insert a num: "))
    t = threading.Thread(target=a_lot_of_calc, args=(num, ))
    t.start() #non-blocking

    num = int(input("Insert a num: "))
    t1 = threading.Thread(target=a_lot_of_calc, args=(num, ))
    t1.start() #non-blocking

    t.join() #blocking
    t1.join()
    print("bye")

