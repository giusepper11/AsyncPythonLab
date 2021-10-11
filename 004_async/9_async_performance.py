import asyncio
import datetime
import math


async def compute(end, start=1):
    pos = start
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


def main():
    print('Starting processing using async')
    el = asyncio.get_event_loop()

    start = datetime.datetime.now()

    # el.run_until_complete(compute(start=1, end=50000000))

    t1 = el.create_task(compute(start=1, end=10000000))
    t2 = el.create_task(compute(start=10000000, end=20000000))
    t3 = el.create_task(compute(start=20000000, end=30000000))
    t4 = el.create_task(compute(start=30000000, end=40000000))
    t5 = el.create_task(compute(start=40000000, end=50000000))

    tasks = asyncio.gather(t1, t2, t3, t4, t5)

    el.run_until_complete(tasks)

    end = datetime.datetime.now() - start

    print(f"Finished in {end.total_seconds():.2f} seconds")


if __name__ == '__main__':
    main()
