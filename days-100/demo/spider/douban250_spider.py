"""


@Author: QiongchaoLi
@Date: 2020/8/8 13:40
"""
import json
import random
import time
from json import JSONEncoder, JSONDecoder

import bs4
import requests
import re

# 要爬的地址
from src.demo import DataBaseUtil

MOVIE_BASE_URL = "https://movie.douban.com/top250"
# 热评基本地址
MOVIE_COMMENT_BASE_URL = 'https://movie.douban.com/subject/'


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/83.0.4103.97 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;'
              'q=0.9,image/webp,image/apng,*/*;'
              'q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8'
}


class MovieEncoder(JSONEncoder):

    def default(self, object):

        if isinstance(object, Movie):

            return object.__dict__

        else:

            # call base class implementation which takes care of

            # raising exceptions for unsupported types

            return json.JSONEncoder.default(self, object)


class MovieDecoder(JSONDecoder):

    def decode(self, o):
        dict = super().decode(o)
        return Movie(dict)


class Movie(object):

    def __init__(self, entries: dict={}):
        for k, v in entries.items():
            if isinstance(v, dict):
                self.__dict__[k] = Movie(v)
            else:
                self.__dict__[k] = v


    def __init__(self, img_url, url, mid, name, second_name, other_name, director, actors, made_year, country, type
                 , score, count_of_comment, quote_info):
        """
        初始化类
        :param img_url:
        :param url:
        :param name:
        :param second_name:
        :param other_name:
        :param actors:
        :param made_year:
        :param country:
        :param type:
        :param score:
        :param count_of_comment:
        :param quote_info:
        """
        self.img_url = img_url
        self.url = url
        self.mid = mid
        self.name = name
        self.second_name = second_name
        self.other_name = other_name
        self.director = director
        self.actors = actors
        self.make_year = made_year
        self.country = country
        self.type = type
        self.score = score
        self.count_of_comment = count_of_comment
        self.quote_info = quote_info


class MovieComments(object):

    def __init__(self, cid, title, title_tip, title_rating, comment_url, content, like, dislike,
                 comment_count, favorite_count, sharing_count, author, author_url, comment_time, movie_id):
        """
        电影评论初始化
        :param cid:
        :param title:
        :param title_tip:
        :param title_rating:
        :param comment_url:
        :param content:
        :param like:
        :param dislike:
        :param comment_count:
        :param favorite_count:
        :param sharing_count:
        :param author:
        :param author_url:
        :param comment_time:
        :param movie_id:
        """
        self.cid = cid
        self.title = title
        self.title_tip = title_tip
        self.title_rating = title_rating
        self.comment_url = comment_url
        self.content = content
        self.like = like
        self.dislike = dislike
        self.comment_count = comment_count
        self.favorite_count = favorite_count
        self.sharing_count = sharing_count
        self.author = author
        self.author_url = author_url
        self.comment_time = comment_time
        self.movie_id = movie_id


# 解析电影
def parse_movie_with_regular():
    movie_list = []
    for page in range(8, 10):
        # 以 f开头表示在字符串内支持大括号内的python 表达式
        url = MOVIE_BASE_URL + f'?start={page * 25}'
        # 发送GET请示
        response = requests.get(url=url, headers=HEADERS)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # 查询所有的li标签
        li_items = soup.select('.article li')
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
            movie_list.append(movie)
        print('完成：', len(movie_list))
        time.sleep(random.randint(3, 5))
    return movie_list


def main():
    movie_list = parse_movie_with_regular()




if __name__ == '__main__':
    main()
