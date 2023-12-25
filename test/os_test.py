
"""
遍历blade-开头的目录，在每个目录下面判断是否有build.gradle，没有就创建
"""
import os
path = os.listdir(os.getcwd())
for p in path:
    if os.path.isdir(p) and p.startswith("blade-"):
        # 进入p目录，然后创建一个名为 build.gradle 的文件
        os.chdir(p)
        file = os.getcwd() + "\\build.gradle"
        print(file)
        if not os.path.exists(file):
            print(p, " not exist")
            f = open("build.gradle", "w")
        os.chdir("..")

