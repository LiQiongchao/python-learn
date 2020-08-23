"""


@Author: QiongchaoLi
@Date: 2020/8/8 13:40
"""
import random
import time

import bs4
import requests

# 要爬的地址
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


class Movie(object):

    def __init__(self, img_url, url, name, second_name, other_name, director, actors, made_year, country, type
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
    for page in range(1):
        # 以 f开头表示在字符串内支持大括号内的python 表达式
        url = MOVIE_BASE_URL + f'?start={page * 25}'
        # 发送GET请示
        response = requests.get(url=url, headers=HEADERS)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        soup.select()


        # 解析标题的a标签
        items = soup.select('.info>div>a')

        for item in items:
            spans = item.find_all('span')
            names = []
            for span in spans:
                name = span.string.replace(' / ', '', 1)
                names.append(name)
            movie_list.append(tuple(names))
        time.sleep(random.randint(1, 5))
    return movie_list


def main():
    list = parse_movie_with_regular()
    for li in list:
        print(li)


if __name__ == '__main__':
    main()
