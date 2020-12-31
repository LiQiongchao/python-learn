"""
时间测试

@Author: QiongchaoLi
@Date: 2020/12/31 9:43
"""

import time

print("time.localtime() = ", time.localtime())

# 格式化成2016-03-20 11:45:39形式
strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(strTime)

# 解析日期
timestamp = time.mktime(time.strptime(strTime,"%Y-%m-%d %H:%M:%S"))
# print(timestamp) # 1609379890.0
print(int(timestamp)) # 1609379890

print(int(time.mktime(time.strptime('2012-12-30 11:25:20',"%Y-%m-%d %H:%M:%S"))))


