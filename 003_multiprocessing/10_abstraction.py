import threading
import time


def execute():
    print("[", end="", flush=True)
    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)
    print("]", flush=True)


if __name__ == "__main__":
    ex = threading.Thread(target=execute)

    ex.start()
    ex.join()
