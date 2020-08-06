"""

@Author: QiongchaoLi
@Date: 2020/8/6 12:44
"""
import builtwith
import ssl
# 查看网站所有者
import whois

# 查看网站使用的技术
parse = builtwith.parse('http://bootcss.com/')
print(parse)
# {'web-servers': ['Nginx'], 'font-scripts': ['Font Awesome'], 'javascript-frameworks': ['Lo-dash', 'Moment.js', 'React', 'Underscore.js', 'Vue.js', 'Zepto', 'jQuery'], 'web-frameworks': ['Twitter Bootstrap']}

ssl._create_default_https_context = ssl._create_unverified_context
print(builtwith.parse('https://www.jianshu.com'))
# {'web-servers': ['Tengine'], 'advertising-networks': ['Google AdSense'], 'web-frameworks': ['Twitter Bootstrap', 'Ruby on Rails'], 'programming-languages': ['Ruby']}

# print(builtwith.parse('https://www.jd.com'))
# {'web-servers': ['Nginx'], 'javascript-frameworks': ['jQuery']}


# who = whois.query('baidu.com')
# print(who.__dict__)



# 解析 robots.txt 使用 robotparser
from urllib import robotparser
parser = robotparser.RobotFileParser()
parser.set_url('https://www.taobao.com/robots.txt')
parser.read()
is_art = parser.can_fetch('Baiduspider', 'http://www.taobao.com/article')
print(is_art) # False
is_pro = parser.can_fetch('Baiduspider', 'http://www.taobao.com/product')
print(is_pro) # False

# taobao-robots.txt
# User-agent: Baiduspider
# Disallow: /
# User-agent: baiduspider
# Disallow: /



