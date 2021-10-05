import queue
import time
import colorama

from threading import Thread
from queue import Queue


def generate(queue: Queue):
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f"Data {i} generated", flush=True)
        time.sleep(2)
        queue.put(i)


def consume(queue: Queue):
    while queue.qsize() > 0:
        value = queue.get()
        print(colorama.Fore.RED + f"Data {value * 2} from {value}", flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    print(colorama.Fore.WHITE + "Program started!", flush=True)
    queue = Queue()
    th1 = Thread(target=generate, args=(queue,))
    th2 = Thread(target=consume, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
