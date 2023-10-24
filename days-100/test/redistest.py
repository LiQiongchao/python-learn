"""
redis operator

@Author: QiongchaoLi
@Date: 2020/8/25 14:34
"""
import redis

TEST_KEY = "hello"


def main():
    redis_conner = redis.Redis()
    redis_conner.set(TEST_KEY, "我是小明")
    # redis 会存储之前会自动使用 utf-8 进行编码，取出来后只需要用 utf-8 解码即可。
    print(redis_conner.get(TEST_KEY).decode('utf-8'))
    redis_conner.delete(TEST_KEY)


if __name__ == '__main__':
    main()


