import datetime
import math

import threading
import multiprocessing


def compute(end, start=1):
    pos = start
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


def main():
    cpus = multiprocessing.cpu_count()
    print(f"Using {cpus} CPUS")

    start = datetime.datetime.now()

    threads = []

    for n in range(1, cpus + 1):
        begin = int(50000000 * (n - 1) / cpus)
        final = int(50000000 * n / cpus)
        print(f"Core {n} processing from {begin} to {final}")
        threads.append(
            threading.Thread(
                target=compute, kwargs={"end": final, "start": begin}, daemon=True
            )
        )

    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    end = datetime.datetime.now() - start
    print(f"Finished in {end.total_seconds():.2f} seconds")


if __name__ == "__main__":
    main()
