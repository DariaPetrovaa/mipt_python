import aiohttp
import asyncio
from aiofile import LineReader, AIOFile, Writer
import re


async def function(f1,f2):
    async with AIOFile(f1, 'r') as f:
        async for line in LineReader(f):
            print(f'I\'m here: {line[:-2:]}')
            async with aiohttp.ClientSession() as session:
                async with session.get(line) as response:
                    html = await response.text()
                    html = re.split(r'[\r\n]', str(html))
                    print(f'Lines starting with <a :')
                    for i in html:
                        if i.strip().startswith('<a '):
                            print(i)
                            async with AIOFile(f2, 'a') as f:
                                writer = Writer(f)
                                await writer(f'{i}\n')
    print('Finished')



loop = asyncio.get_event_loop()
with open('res.txt','w') as f:
    pass
loop.run_until_complete(function("urls.txt",'res.txt'))


