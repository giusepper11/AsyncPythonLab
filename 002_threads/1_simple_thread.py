import threading
import time


def count(what, many):
    for n in range(1, many + 1):
        print(f"{n} {what}(s)")
        time.sleep(1)


def main():
    th = threading.Thread(target=count, args=("elephant", 10))

    th.start()  # Add thread to thread pool
    print("Program will continue to here meanwhile thread is running")

    th.join()  # Awaits the thread to finish execution

    print("End")


if __name__ == "__main__":
    main()
