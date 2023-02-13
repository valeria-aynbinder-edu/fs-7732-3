import time


def wait_using_sleep(sec):
    print("Counting down")
    time.sleep(sec)
    print(f"{sec} seconds is over")


# busy wait
def wait_wasting_cpu(sec):
    print("Counting down")
    start = time.time()
    while time.time()-start < sec:
        continue
    print(f"{sec} seconds is over")


if __name__ == '__main__':
    # wait_using_sleep(50)
    wait_wasting_cpu(50)