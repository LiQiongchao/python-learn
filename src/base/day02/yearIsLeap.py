
"""
根据输入年份判断是不是闰年
如果是闰年输出 true，否则 false
"""

year = int(input('请输入年份：'))
print('是不是闰年：' , year % 4 == 0 and year % 100 != 0 or year % 400 ==0)


