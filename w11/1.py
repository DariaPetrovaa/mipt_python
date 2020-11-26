import asyncio
import aiohttp
from concurrent.futures import ALL_COMPLETED

async def func(session,url):
    async with session.get(url) as response:
        html = await response.text()
        return html

async def main_f(n):
    async with aiohttp.ClientSession() as session:
        res = await asyncio.wait({func(session,'http://127.0.0.1:8000')for i in range(n)},return_when = ALL_COMPLETED) 
        for i in res[0]:
            print(i.result())
        print('Finished')

loop = asyncio.get_event_loop()
loop.run_until_complete(main_f(100))

