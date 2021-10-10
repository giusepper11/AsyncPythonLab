import multiprocessing


def deposit(balance):
    for _ in range(10000):
        balance.value += 1


def withdraw(balance):
    for _ in range(10000):
        balance.value -= 1


def perform_transactions(balance):
    pc1 = multiprocessing.Process(target=withdraw, args=(balance,))
    pc2 = multiprocessing.Process(target=withdraw, args=(balance,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


if __name__ == "__main__":
    balance = multiprocessing.Value("i", 100)
    print(f"Initial balance: {balance.value}")

    for _ in range(10):
        perform_transactions(balance)

    print(f"Final balance: {balance.value}")
