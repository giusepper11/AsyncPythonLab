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


async def main():
    total = 5000
    data = asyncio.Queue()
    print(f"computing {total * 2:.2f} data.")

    await generate_data(total, data)
    await generate_data(total, data)
    await process_data(total * 2, data)


if __name__ == "__main__":
    el = asyncio.get_event_loop()

    el.run_until_complete(main())
    el.close()
