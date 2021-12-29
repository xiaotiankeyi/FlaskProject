from flask import Flask
from flask import Response

"""
cookies作用,解决服务端和客户端无状态链接的问题
特征: 有效期,域名概念
"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')


@app.route("/")
def index():
    """创建返回对象"""
    res = Response("返回对象")

    """设置cookies
        max_age=None,   最大存活时间(s)
        expires=None,   通过datetime设置准确时间
        path="/",
        domain=None,    设置子域名的cookies
    """

    res.set_cookie('name', 'jack')

    """删除cookies"""
    res.delete_cookie("")

    return res


if __name__ == "__main__":
    app.run()
