import os

from flask import Flask, request, redirect, g, sessionObj, url_for

"""
@app.before_first_request
"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.secret_key = os.urandom(24)


@app.route("/")
def index():
    if hasattr(g, 'name'):
        print(f'g值等于{g.name}')
        return """
                <p>登录成功后的首页<p>
                """
    else:
        return """
                <p>未登录前首页</p>
                <a href="/login/">点击跳转登录页面</a>
                """


@app.route("/login/", methods=['get', 'post'])
def login():
    if request.method == 'POST':
        sessionObj['username'] = request.form['params']
        return redirect(url_for('index'))
    else:
        return """
                <a>首页<a>
                <form action='/login/' method='post'>
                    <input type='text' name='params' value=''><br>
                    <input type='submit' value='提交'>
                <form>
                """


# @app.before_first_request
# def input():
#     print("项目第一次请求开始时执行该函数")

@app.before_request
def before_request():
    print('请求前执行')
    username = sessionObj.get('username')
    print(username)
    if username:
        g.name = username


if __name__ == "__main__":
    app.run()
