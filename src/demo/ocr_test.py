"""
OCR 识别
参考：https://zhuanlan.zhihu.com/p/342686109
注意：
    - 无法识别 C:/xx 和 C:\ 开头的文件目录。需要是 C:\\ 开头。

@Author: QiongchaoLi
@Date: 2022/5/20 10:13
"""

import easyocr

# 创建reader对象
reader = easyocr.Reader(lang_list = ['ch_sim', 'en'])
# 读取图像
# result = reader.readtext(image='135.jpg') # 无法识别
# result = reader.readtext('C:\\Users/xx/Desktop/135.jpg')
# [([[10, 12], [240, 12], [240, 42], [10, 42]], '识别的结果包含在元组里', 0.8547509729123624), ([[250, 12], [520, 12], [520, 40], [250, 40]], '元组由三部分组成:  边框坐标', 0.5805319218934396), ([[530, 14], [578, 14], [578, 38], [530, 38]], '文本', 0.6901296445827629), ([[590, 14], [684, 14], [684, 38], [590, 38]], '识别概率。', 0.9394764487292191), ([[8, 72], [106, 72], [106, 102], [8, 102]], '关于语言:', 0.9376084843378261)]

# result = reader.readtext('C:\\Users/Qiongchao/Desktop/123.png')
result = reader.readtext('D:\\WorkSpaces\\practise-projects\\python-learn\\src\\static\\img\\123.png')

# 提取结果
for i in result:
    word = i[1]
    print(word)

