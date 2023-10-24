"""
利用生成式（推导式）的用法

@Author: QiongchaoLi
@Date: 2020/8/3 12:52
"""

# 生成式可以生成列表，集合和字典
prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {key: val for key, val in prices.items() if val > 100}
print(prices2)

