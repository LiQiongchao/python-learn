"""
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注

@Author: QiongchaoLi
@Date: 2020/7/13 12:48
"""
from random import randint

money = 1000

while money > 0:
    print("Your total money is ", money)
    needGoOn = False
    while True:
        stake = int(input('请下注：'))
        if 0 < stake <= money:
            break
    first = randint(1, 6) + randint(1, 6)
    print('玩家揺出了：', first)
    if first == 7 or first == 11:
        print('玩家胜！')
        money += stake
    elif first == 2 or first == 3 or first == 12:
        print('庄家胜！')
        money -= stake
    else:
        needGoOn = True
    while needGoOn:
        current = randint(1, 6) + randint(1, 6)
        print('玩家揺出了：', current)
        needGoOn = False
        if current == first:
            print('玩家胜！')
            money += stake
        elif current == 7:
            print('庄家胜！')
            money -= stake
        else:
            needGoOn = True
print('你破产了！')