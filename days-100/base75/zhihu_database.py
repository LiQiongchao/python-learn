"""
知乎数据入数据库

@Author: QiongchaoLi
@Date: 2020/8/8 23:02
"""
import hashlib
import pickle
import re
import zlib
from urllib.parse import urljoin

import bs4
import pymysql
import requests

connect = pymysql.connect(host='127.0.0.1', port=3306, database='web_crawler', password='root', user='root'
                          , charset='utf8', autocommit=True)


# 入库
def write_to_db(name, url, page, digest):
    try:
        with connect.cursor() as cursor:
            cursor.execute('insert into zh_explore(name, url, page, digest) values (%s, %s, %s, %s)', (name, url, page, digest))
    except pymysql.MySQLError as err:
        print(err)


def main():
    base_url = 'https://www.zhihu.com/'
    seed_url = urljoin(base_url, 'explore')
    headers = {'user-agent': 'Baiduspider'}
    try:
        response = requests.get(seed_url, headers=headers)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        href_regex = re.compile(r'^/question')
        a_tags = soup.find_all('a', {'href': href_regex})
        for a_tag in a_tags:
            href = a_tag.attrs['href']
            name = a_tag.get_text()
            find_url = urljoin(base_url, href)
            # 摘要
            digest = hashlib.sha1(find_url.encode()).hexdigest()
            html_page = requests.get(find_url, headers=headers).text
            # 夺缩链接地址的页面
            zipped_page = zlib.compress(pickle.dumps(html_page))
            write_to_db(name, find_url, zipped_page, digest)
    finally:
        connect.close()


if __name__ == '__main__':
    main()
