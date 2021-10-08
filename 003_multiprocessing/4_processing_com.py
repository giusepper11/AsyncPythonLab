import multiprocessing


def ping(conn):
    conn.send("Ping!")


def pong(conn):
    msg = conn.recv()
    print(f"{msg} >>> Pong!")


def main():
    conn1, conn2 = multiprocessing.Pipe(duplex=True)  # for by direcional conn

    p1 = multiprocessing.Process(target=ping, args=(conn1,))
    p2 = multiprocessing.Process(target=pong, args=(conn2,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
