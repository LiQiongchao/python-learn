
"""
根据用户输入的账号密码来判断是否登录成功
"""

username = input("please type in your username: ")
password = input("please type in your password: ")

# python 使用缩进符来表示层次
if username == 'admin' and password == '123456':
    print("登录成功")
else:
    print("登录失败")



