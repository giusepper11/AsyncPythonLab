import multiprocessing


def calculate(data):
    print(f"Calculating {data} **")
    return data ** 2


def main():
    pool_size = multiprocessing.cpu_count() * 2

    pool = multiprocessing.Pool(processes=pool_size)

    entrypoint = list(range(7))

    outputs = pool.map(func=calculate, iterable=entrypoint)

    print(f"output: {outputs}")

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
