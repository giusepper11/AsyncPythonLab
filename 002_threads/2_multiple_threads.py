import threading
import time


def count(what, many):
    for n in range(1, many + 1):
        print(f"{n} {what}(s)")
        time.sleep(1)


def main():
    threads = [
        threading.Thread(target=count, args=("elephant", 10)),
        threading.Thread(target=count, args=("hole", 10)),
        threading.Thread(target=count, args=("house", 10)),
        threading.Thread(target=count, args=("money", 10)),
        threading.Thread(target=count, args=("ducks", 10)),
    ]

    [th.start() for th in threads]

    print("Program will continue to here meanwhile thread is running")

    [th.join() for th in threads]

    print("End")


if __name__ == "__main__":
    main()
