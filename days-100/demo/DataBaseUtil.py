"""
数据库连接工具

@Author: QiongchaoLi
@Date: 2020/8/23 15:53
"""
import pymysql
import redis as redis

MYSQL_HOST = 'localhost'
MYSQL_USERNAME = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_PORT = 3306


# mysql连接
def mysql_connector(database='web_crawler'):
    return pymysql.Connection(host=MYSQL_HOST, user=MYSQL_USERNAME, password=MYSQL_PASSWORD, database=database, port=MYSQL_PORT
                              , charset='UTF8', autocommit=True)


# redis连接
def redis_connector():
    return redis.Redis(host='192.168.31.120', password='HelloLee')

