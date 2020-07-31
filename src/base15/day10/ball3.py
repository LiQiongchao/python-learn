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

def main():
    # 初始化 pygame中的模块
    pygame.init()
    # 初始化显示的窗口并设置窗口尺寸
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('大球吃小球')

    # 绘制一个圆(参数分别是: 屏幕, 颜色, 圆心位置, 半径, 0表示填充圆)
    # pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)
    # 加载图片
    # ball_image = pygame.image.load('./res/ball.png')
    # 在窗口上渲染图像
    # screen.blit(ball_image, (50, 50))
    # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
    # pygame.display.flip()

    # 定义变量来表示小球在屏幕上的位置
    x, y = 50, 50

    running = True
    # 开启一个事件的循环处理
    while running:
        # 从消息队列中获取事件并对事件进行处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        # 设置窗口的背景色(颜色是由红绿蓝三原色构成的元组)
        screen.fill((255, 255, 255))
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 30, 0)

        # 刷新当前窗口(渲染窗口将绘制的图像呈现出来)
        pygame.display.flip()
        # 每隔50毫秒就改变小球的位置再刷新窗口
        pygame.time.delay(50)
        x, y = x + 5, y + 5


if __name__ == '__main__':
    main()


