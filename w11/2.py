import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp
from collections import namedtuple

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)

async def fetch_ip(session,service):
      async with session.get(service.url) as response:
        html = await response.json()
        return html
    

async def asynchronous():
    async with aiohttp.ClientSession() as session:
        fut  = await asyncio.wait({fetch_ip(session,serv) for serv in SERVICES},return_when = FIRST_COMPLETED)
        for i in fut[0]:
            a = i.result()
            for serv in SERVICES:
                try:
                    print(a[serv.ip_attr])
                except:
                    pass



ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())

