"""
爬取话单日志

@Author: QiongchaoLi
@Date: 2020/8/8 13:40
"""
import json
import random
import time
from http.cookiejar import CookieJar

import bs4
import requests
import re

# 要爬的地址
from src.demo import DataBaseUtil

URL = "http://api.pjxx866.com/web/admio/a_calllog.aspx"


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


# 解析话单
def parse_call_log():
    cookies = {"ASP.NET_SessionId": "bfeomwh504t1ueqm3vf1jboh"}
    log_list = []
    # 以 f开头表示在字符串内支持大括号内的python 表达式
    response = requests.post(url=URL, headers=HEADERS, cookies=cookies)
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    # 查询所有的table子标签，第一个为标题
    tbody_items = soup.select('.update tbody')
    print(tbody_items)
    return
    for item in li_items:
        # 解析图片
        img_url = item.find_all('img', limit=1)[0].attrs['src']
        info_divs = item.select('.info > div')
        # 解析标题
        linka = info_divs[0].find('a')
        url = linka.attrs['href']
        names = linka.find_all('span')
        # 解析内容
        profile = info_divs[1].select_one('p').text.strip().split('\n')
        mans = profile[0].split('   ')
        director = mans[0].strip()[3:]
        actors = mans[1].strip()[3:] if len(mans) > 1 else ''
        # 解析日期，国家
        span3 = profile[1].strip().split(' / ')
        # 解析评分，评价人数，简介
        score_spans = info_divs[1].find_all('span')
        pattern = re.compile('\d*')
        quote_obj = info_divs[1].find('span', 'inq')
        quote = quote_obj.text if hasattr(quote_obj, 'text') else ''
        mid_url = url[:len(url) - 1]
        mid_star_index = mid_url.rindex('/') + 1
        mid = mid_url[mid_star_index:]

        movie = Movie(img_url, url, mid, names[0].text.strip(), names[1].text.replace('/', '', 1).strip(),
                      (names[2].text.replace('/', '', 1).strip()) if (len(names) > 2) else '', director,
                      actors, span3[0], span3[1], span3[2], score_spans[1].text,
                      pattern.match(score_spans[3].text).group(), quote)

        mysql_connector = DataBaseUtil.mysql_connector()
        cursor = mysql_connector.cursor()
        sql = (
            'INSERT INTO `web_crawler`.`douban_movies`(`mid`, `name`, `url`, `second_name`, `other_name`, `img_url`, `director`, `actors`, `made_year`, `score`, `count_of_comment`, `intro`) '
            'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);')
        cursor.execute(sql, (movie.mid, movie.name,
                             movie.url, movie.second_name, movie.other_name, movie.img_url, movie.director,
                             movie.actors,
                             movie.make_year, movie.score, movie.count_of_comment, movie.quote_info))
        # 最后插入行的主键id
        # print(cursor.lastrowid)
        # 最新插入行的主键id
        movie.id = mysql_connector.insert_id()
        redis_connector = DataBaseUtil.redis_connector()
        redis_connector.hset('douban:movie:top250', movie.id, MovieEncoder().encode(movie))
        time.sleep(random.randint(3, 5))


def main():
    parse_call_log()


if __name__ == '__main__':
    main()
