import multiprocessing

print(f"Process with name : {multiprocessing.current_process().name}")


def do_something(value):
    print(f"working on: {value}")


def main():
    pc = multiprocessing.Process(
        target=do_something, args=("bird",), name="sample_proc"
    )

    print(f"Start process with name: {pc.name}")

    pc.start()
    pc.join()


if __name__ == "__main__":
    main()
