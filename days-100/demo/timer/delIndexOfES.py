"""
定期删除7天前es的索引
@Author: QiongchaoLi
@Date: 2020/11/16 16:41
"""
import datetime

# 要删除日期的后缀
import json

import requests

# 服务地址
ES_SERVER='http://127.0.0.1:9201/'
DEL_TIME=(datetime.datetime.now()+datetime.timedelta(days=-7)).strftime("%Y.%m.%d")
INDEX_PREFIX=[
    '.monitoring-kibana-6-', # kibana监控
    '.monitoring-es-6-', # es 监控
    'logstash-bus-dev-', # bus开发环境的日志
    'logstash-bus-customer-test-', # bus-customer模块 测试环境的日志
    'logstash-bus-receiver-test-', # bus-receiver模块 测试环境的日志
    'logstash-bus-customer-online-', # bus-customer模块 生产环境的日志
    'logstash-bus-receiver-online-', # bus-receiver模块 生产环境的日志
]


def main():
    print('-----------------------------------'+DEL_TIME+' Clear index of ES -------------------------------')
    for prefix in INDEX_PREFIX:
        index = prefix + DEL_TIME
        response = requests.delete(ES_SERVER + index)
        print('del index [' + index + '], response ' + response.text)


if __name__ == '__main__':
    main()


