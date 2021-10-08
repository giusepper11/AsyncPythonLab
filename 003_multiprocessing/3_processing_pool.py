import multiprocessing


def calculate(data):
    print(f"Working with process: {multiprocessing.current_process().name}")
    return data ** 2


def main():
    pool_size = multiprocessing.cpu_count() * 2

    pool = multiprocessing.Pool(processes=pool_size)

    entrypoint = list(range(13))

    outputs = pool.map(func=calculate, iterable=entrypoint)

    print(f"output: {outputs}")

    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
