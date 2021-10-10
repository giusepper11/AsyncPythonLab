import time

from concurrent.futures.process import ProcessPoolExecutor as Executor

# from concurrent.futures.thread import ThreadPoolExecutor as Executor


def execute():
    print("[", end="", flush=True)
    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)
    print("]", flush=True)


if __name__ == "__main__":
    with Executor() as ex:
        ex.submit(execute)
