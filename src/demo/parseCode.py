"""


@Author: QiongchaoLi
@Date: 2021/7/10 10:07
"""

def main():
    code = "@@3@19e580b81275"
    for i in range(10):
        newCode1 = code.replace("@", str(i), 1)
        # print(newCode1)
        for i in range(10):
            newCode2 = newCode1.replace("@", str(i), 1)
            for i in range(10):
                newCode3 = newCode2.replace("@", str(i), 1)
                print(newCode3)


if __name__ == '__main__':
    main()

