"""

@Author: QiongchaoLi
@Date: 2020/7/30 16:37
"""
import pygame


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

