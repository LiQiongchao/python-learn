
"""
英制单位英寸和公制单位厘米的互换

@Author: QiongchaoLi
@Date: 2020/7/12 10:30
"""

print("请选择单位\n 1: 英寸, 2: 厘米")
unit = int(input())
value = float(input("请输入长度： "))

if unit == 1:
    print("%f英寸 = %f厘米" %(value, value * 2.54))
elif unit == 2:
    print("$f厘米 = %f英寸" %(value, value / 2.54))
else:
    print('please type valid unit')








