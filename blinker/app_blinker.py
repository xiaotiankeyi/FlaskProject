import datetime

import blinker
from flask import Flask, g, request, redirect

"""
blinker信号机制
1、自定义信号机制
    创建信号,监听一个信号,发送一个信号
"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')


@app.route("/", methods=['get', 'post'])
def index():
    if request.method == 'POST':
        g.name = request.form['params']
        return redirect('/')
    else:
        return """
                <a>首页<a>
                <form action='/' method='post'>
                    <input type='text' name='params' value=''><br>
                    <input type='submit' value='提交'>
                <form>
                """


# 创建信号
signal = blinker.Namespace()
send_signal = signal.signal("登录信息使用场景")


# 监听信号
def loginLog(val):
    username = g.name
    now = datetime.datetime.now()
    ipAddress = request.remote_addr
    LogData = f"用户:{username},通过ip为{ipAddress}的地址在{now}时间点登录服务"
    with open('LoginLog.txt', mode='a') as f:
        f.write(LogData + "\n")
        f.close()


send_signal.connect(loginLog)


@app.route("/login/<name>/")
def login(name):
    """发送信号的函数"""
    print(name)
    if name != '' and name != None:
        g.name = name
        # 发送信号
        send_signal.send()
        return "登录成功！！"
    else:
        return "请输入正确的登录用户"
    # return name


if __name__ == "__main__":
    app.run()
