import multiprocessing


def ping(qeue):
    qeue.put("Ping!")


def pong(qeue):
    msg = qeue.get()
    print(f"{msg} >>> Pong!")


def main():
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
