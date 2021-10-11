import asyncio


async def say_hello_with_delay():
    print("Hello....")
    await asyncio.sleep(2)

    print("all....")


if __name__ == "__main__":
    el = asyncio.get_event_loop()
    el.run_until_complete(say_hello_with_delay())
    el.close()
