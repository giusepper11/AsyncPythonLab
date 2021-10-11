import compute
import datetime


def main():
    start = datetime.datetime.now()

    compute.compute(end=50000000)

    end = datetime.datetime.now() - start
    print(f"Finished in {end.total_seconds():.2f} seconds")


if __name__ == "__main__":
    main()
