# 《Python编程：从入门到实践（第2版）》

# 第一部分 基本知识
## 配置 sublime 运行环境
### 配置
单击Sublime Text图标以启动它，也可在搜索栏中输入Sublime Text来找到它再
启动。选择菜单Tools ▶ Build System ▶ New Build System，新建一个配置文件。删
除该文件中的所有内容，再输入如下内容：
```
{
    "cmd": ["python3", "-u", "$file"],
}
```
> 选择对应的python环境变量的命令，有的直接配置的是 python

然后保存默认打开的文件夹中，命名为Python3.sublime-build

### 运行
新建 hello_python.py
```python
print("Hello Python world!")
```
在你的系统中，如果能使用命令python 来启动Python 3(刚才配置的文件名)，可以选择菜单Tools ▶
Build或按Ctrl + B（在macOS系统中为Command + B）来运行程序。

如果需要像前一节那样配置Sublime Text，请选择菜单Tools ▶ Build System ▶ Python 3来运行这个程
序。从此以后，你就可以选择菜单Tools ▶ Build或按Ctrl + B（或Command + B）来运
行程序了。




