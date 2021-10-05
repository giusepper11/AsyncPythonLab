import threading
import random
import time

from typing import List


class Account:
    def __init__(self, balance=0) -> None:
        self.balance = balance


def services(accounts, total):
    for _ in range(1, 10000):
        c1, c2 = take_two_accounts(accounts)
        value = random.randint(1, 100)
        transfer(c1, c2, value)
        validate_data(accounts, total)


def take_two_accounts(accounts: List[Account]):
    c1 = random.choice(accounts)
    c2 = random.choice(accounts)

    while c1 == c2:
        c2 = random.choice(accounts)

    return c1, c2


def create_accounts() -> List[Account]:
    return [Account(balance=random.randint(5000, 10000)) for _ in range(1, 6)]


def transfer(origin: Account, destination: Account, amount: int):
    if origin.balance < amount:
        return
    origin.balance -= amount
    time.sleep(0.001)
    destination.balance += amount


def validate_data(accounts: List[Account], total: int):
    actual = sum(account.balance for account in accounts)
    if actual != total:
        print(
            f"ERROR, inconsistent bank data. actual: R${actual:.2f} vs total: R${total:.2f}",
            flush=True,
        )
    else:
        print(f"All good, R${actual:.2f} vs total: R${total:.2f}", flush=True)


def main():
    accounts = create_accounts()
    total = sum(account.balance for account in accounts)
    print("Starting transfers...")

    tasks = [
        threading.Thread(target=services, args=(accounts, total)) for _ in range(1, 10)
    ]

    [task.start() for task in tasks]
    [task.join() for task in tasks]

    print("Ended transfers!")
    validate_data(accounts, total)


if __name__ == "__main__":
    main()
