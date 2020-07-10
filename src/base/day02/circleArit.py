import math

"""
输入圆的半径，计算周长与面积
"""
f = float(input('请输入圆的半径：'))

tl = math.pi * f * 2
m = math.pi * f * f
print("圆的周长：%.2f" %(tl))
print("圆的面积：%.2f" %(m))



