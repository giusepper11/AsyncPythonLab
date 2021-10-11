import asyncio
import aiofiles


async def example_read():
    async with aiofiles.open("text.txt") as f:
        content = await f.read()
    print(content)


async def example_readline():
    async with aiofiles.open("text.txt") as f:
        async for line in f:
            print(line)


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(example_read())
    el.close()


if __name__ == "__main__":
    main()
