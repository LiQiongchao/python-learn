"""

@Author: QiongchaoLi
@Date: 2020/8/7 13:47
"""
import re

pattern = re.compile(r'<a\s+[^>]*?href="(.*?)"\s*[^>]*?>')
context = '<li class="item"><a target="_blank" href="http://data.sports.sohu.com/nba/nba_schedule_by_day.html">直播</a></li>'
str = pattern.search(context)
# while str:
#     print(str.group())
#     str = pattern.search(context, str.end())

# group  0是匹配整体，1|2|3是匹配正则里面"()"中相匹配的内容，如group(1) 匹配的是href里面 (.*?)
# <a target="_blank" href="http://data.sports.sohu.com/nba/nba_schedule_by_day.html">
print(str.group(0))
# http://data.sports.sohu.com/nba/nba_schedule_by_day.html
print(str.group(1))
