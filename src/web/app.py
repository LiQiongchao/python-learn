"""
使用web flask

@Author: QiongchaoLi
@Date: 2020/8/17 16:04
"""
from flask import Flask, request

app = Flask(__name__)


# 主页
@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return """<form action="signin" method="post">
    <p><input name="username"></p>
    <p><input name="password" type="password"></p>
    <p><button type="submit">Sign In</button></p>
    </form>"""


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request中读取表单内容
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


def main():
    # 默认监听5000端口
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()
