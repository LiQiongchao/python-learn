"""

@Author: QiongchaoLi
@Date: 2020/8/6 13:40
"""
import re

LI_A_PATTERN = re.compile(r'<li class="item">.*?</li>')
A_TEXT_PATTERN = re.compile(r'<a\s+[^>]*?(.*?)</a>')
A_HREF_PATTERN = re.compile(r'<a\s+[^>]*?href="(.*?)"\s*[^>]*?>')


def start_crawl(seed_url, pattern, max_depth):
    pass


def main():
    start_crawl(seed_url = 'http://sports.sohu.com/nba_a.shtml', pattern=LI_A_PATTERN, max_depth = 2)

if __name__ == '__main__':
    main()


