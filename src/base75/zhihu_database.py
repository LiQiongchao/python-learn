"""
知乎数据入数据库

@Author: QiongchaoLi
@Date: 2020/8/8 23:02
"""

import pymysql


connect = pymysql.connect(host='127.0.0.1', port='3306', database='web_crawler', password='root', user='root')

