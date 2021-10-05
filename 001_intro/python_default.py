import datetime
import math


def compute(end, start=1):
    pos = start
    factor = 1000 * 1000
    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


def main():
    start = datetime.datetime.now()

    compute(end=50000000)

    end = datetime.datetime.now() - start
    print(f"Finished in {end.total_seconds():.2f} seconds")


if __name__ == "__main__":
    main()
