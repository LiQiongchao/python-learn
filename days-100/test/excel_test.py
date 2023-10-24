"""

@Author: QiongchaoLi
@Date: 2020/9/22 12:33
"""
from openpyxl import Workbook

def testAppend():
    wb = Workbook()
    ws = wb.active
    for row in range(1, 40):
        ws.append(range(600))

    wb.save("test1.xlsx")


if __name__ == '__main__':
    list = [1,2,3]
    print(len(list))