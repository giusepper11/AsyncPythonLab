import multiprocessing
import time


def func1(val: int, status: bool):
    if status:
        res = val + 10
        status = False
    else:
        res = val + 20
        val = 200
        status = True

    print(f"Result of func1 is {res}")
    time.sleep(0.001)


def func2(val: int, status: bool):
    if status:
        res = val + 30
        status = False
    else:
        res = val + 40
        val = 400
        status = True

    print(f"Result of func2 is {res}")
    time.sleep(0.001)


def main():
    value = 0
    state = False

    p1 = multiprocessing.Process(target=func1, args=(value, state))
    p2 = multiprocessing.Process(target=func2, args=(value, state))

    # Both Process will not share nothing
    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
