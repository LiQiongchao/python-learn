
# 摄氏温度转成华氏温度

c = float(input("请输入摄氏温度："))
f = (c + 32) * 1.8

# %.1f 表示保留一位小数点
print('%.1f摄氏温度 = %.1f华氏温度' %(c,f))
# 写法二：
print(f'{c:.1f}摄氏温度 = {f:.1f}华氏温度')
