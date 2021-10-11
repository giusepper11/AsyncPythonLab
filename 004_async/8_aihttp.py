import asyncio

import aiofiles
import aiohttp
import bs4


async def get_links():
    links = []
    async with aiofiles.open("links.txt") as f:
        async for link in f:
            links.append(link.strip())
    return links


async def get_html(link):
    print(f"getting html from {link}")
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            resp.raise_for_status()
            return await resp.text()


def get_page_title(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    title = soup.select_one("title").text

    title = title.split("|")[0].strip()
    return title


async def print_title():
    links = await get_links()
    tasks = []

    for link in links:
        tasks.append(asyncio.create_task(get_html(link)))

    for task in tasks:
        html = await task
        title = get_page_title(html)

        print(f"Course: {title}")


def main():
    el = asyncio.get_event_loop()
    el.run_until_complete(print_title())
    el.close()


if __name__ == "__main__":
    main()
