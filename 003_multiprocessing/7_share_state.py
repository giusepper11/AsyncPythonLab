import multiprocessing
import time
import ctypes


def func1(val: int, status: bool):
    if status.value:
        res = val.value + 10
        status.value = False
    else:
        res = val.value + 20
        val.value = 200
        status.value = True

    print(f"Result of func1 is {res}")
    time.sleep(0.001)


def func2(val: int, status: bool):
    if status.value:
        res = val.value + 30
        status.value = False
    else:
        res = val.value + 40
        val.value = 400
        status.value = True

    print(f"Result of func2 is {res}")
    time.sleep(0.001)


def main():
    value = multiprocessing.Value("i", 0)
    state = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=func1, args=(value, state))
    p2 = multiprocessing.Process(target=func2, args=(value, state))

    # Both Process will share!!
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
