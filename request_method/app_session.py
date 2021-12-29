import os
from flask import Flask
from flask import Response
from flask import request
from flask import session
from datetime import timedelta

"""
cookies作用,解决服务端和客户端无状态链接的问题
特征: 有效期,域名概念
"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')
app.secret_key = os.urandom(12)
# app.config['PERMANENT_session_LIFETIME'] = timedelta(hours=2)

@app.route("/")
def index():
    """设置session"""
    session.permanent = True    # 设置session有效期默认31天后过期
    session['username'] = 'jack'
    session['password'] = 123456
    res = Response("返回了sessionObj", status=200)
    return res


@app.route('/getsession/')
def getsession():
    username = session.get('username')
    a = request.headers['Cookie']
    return f'cookies:{a},\nusername:{username}' or '没有sessionObj'


@app.route("/delsession/")
def deleteSsssion():
    """删除指定的session"""
    session.pop("username")
    """删除所有"""
    # sessionObj.clear()

    return '<p>删除了session中的username<P>'


if __name__ == "__main__":
    app.run()
