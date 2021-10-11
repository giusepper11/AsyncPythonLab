from typing import Generator


def fibo() -> Generator[int, None, None]:
    value = 0
    next_value = 1

    while True:
        value, next_value = next_value, value + next_value
        yield value


if __name__ == "__main__":

    for n in fibo():
        print(n, end=", ")
        if n > 100:
            break
    print("\n END!")
