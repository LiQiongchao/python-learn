"""
异步加请求
使用`get_event_loop`函数获得系统默认的事件循环，通过`gather`函数可以获得一个`future`对象，
`future`对象的`add_done_callback`可以添加执行完成时的回调函数，`loop`对象的`run_until_complete`方法
可以等待通过`future`对象获得协程执行结果。


@Author: QiongchaoLi
@Date: 2020/8/4 13:19
"""
import asyncio
import re

import aiohttp as aiohttp

PATTERN = re.compile(r'\<title\>(?P<title>.*)\<\/title\>')


async def fetch_page(session, url):
    async with session.get(url, ssl=False) as resp:
        return await resp.text()


async def show_title(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_page(session, url)
        print(PATTERN.search(html).group('title'))


def main():
    urls = ('https://www.python.org/',
            'https://git-scm.com/',
            'https://www.jd.com/',
            'https://www.taobao.com/',
            'https://www.douban.com/')
    loop = asyncio.get_event_loop()
    cos = [show_title(url) for url in urls]
    loop.run_until_complete(asyncio.wait(cos))
    loop.close()


if __name__ == '__main__':
    main()
