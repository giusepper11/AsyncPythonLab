import datetime
import asyncio


async def generate_data(amount: int, data: asyncio.Queue):
    print(f"Await data generation of {amount} data")
    for idx in range(1, amount + 1):
        item = idx * idx
        await data.put((item, datetime.datetime.now()))
        await asyncio.sleep(0.001)
    print(f"{amount} data generated successfully")


async def process_data(amount: int, data: asyncio.Queue):
    print(f"Await process of {amount} data")
    processed = 0
    while processed < amount:
        await data.get()
        processed += 1
        await asyncio.sleep(0.001)
    print(f"was processed {processed} items")


def main():
    total = 5000
    data = asyncio.Queue()
    print(f"computing {total * 2:.2f} data.")

    el = asyncio.get_event_loop()

    t1 = el.create_task(generate_data(total, data))
    t2 = el.create_task(generate_data(total, data))
    t3 = el.create_task(process_data(total * 2, data))

    tasks = asyncio.gather(t1, t2, t3)

    el.run_until_complete(tasks)


if __name__ == "__main__":
    main()
