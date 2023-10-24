"""
大球吃小球游戏
Pygame是一个开源的Python模块，专门用于多媒体应用（如电子游戏）的开发，其中包含对图像、声音、视频、事件、碰撞等的支持。
Pygame建立在[SDL](https://zh.wikipedia.org/wiki/SDL)的基础上，SDL是一套跨平台的多媒体开发库，用C语言实现，
被广泛的应用于游戏、模拟器、播放器等的开发。而Pygame让游戏开发者不再被底层语言束缚，可以更多的关注游戏的功能和逻辑。

@Author: QiongchaoLi
@Date: 2020/7/29 16:58
"""
from enum import Enum, unique
from math import sqrt
from random import randint
import pygame


@unique
class Color(Enum):

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GRAY = (242, 242, 242)

    @staticmethod
    def random_color():
        """随机颜色"""
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

class Ball(object):

    def __init__(self, x, y, radius, sx, sy, color=(Color.RED)):
        """初始方法"""
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = sx
        self.sy = sy
        self.color = color
        self.alive = True

    def move(self, screen):
        """move"""
        self.x += self.sx
        self.y += self.sy
        if self.x - self.radius <= 0 or self.x + self.radius >= screen.get_width():
            self.sx = -self.sx
        if self.y - self.radius <= 0 or self.y + self.radius >= screen.get_height():
            self.sy = -self.sy

    def eat(self, other):
        if self.alive and other.alive and self != other:
            dx, dy = self.x - other.x, self.y - other.y
            distance = sqrt(dx ** 2 + dy ** 2)
            if distance < self.radius + other.radius and self.radius > other.radius:
                other.alive = False
                self.radius = self.radius + int(other.radius * 0.146)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius, 0)



def main():
    # 定义用来装所有球的容器
    balls = []
    # 初始化 pygame中的模块
    pygame.init()
    # 初始化显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')

    running = True
    # 开启一个事件的循环处理
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            # 点右上角退出键，退出游戏
            if event.type == pygame.QUIT:
                print('接收到退出')
                running = False
            # 处理鼠标事件
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # 获取鼠标的位置
                x, y = event.pos
                radius = randint(10, 100)
                sx, sy = randint(-10, 10), randint(-10, 10)
                color = Color.random_color()
                # 在点击鼠标的位置创建一个球（大小，速度和颜色随机）
                ball = Ball(x, y, radius, sx, sy, color)
                # 将球添加到列表容器中
                balls.append(ball)
        # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
        screen.fill((255, 255, 255))
        # 取出容器的球，如果没被吃掉就绘制，被吃掉就移除
        for ball in balls:
            if ball.alive:
                ball.draw(screen)
            else:
                balls.remove(ball)
        pygame.display.flip()
        # 每隔50毫秒就改变球的位置再刷新容器
        pygame.time.delay(50)
        for ball in balls:
            ball.move(screen)
            # 检查球有没有吃到其它球
            for other in balls:
                ball.eat(other)


if __name__ == '__main__':
    main()


