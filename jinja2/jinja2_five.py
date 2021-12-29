from flask import Flask
from flask import render_template

"""
include标签的使用
1、相当于是直接将指定的模板中的代码复制到当前位置
2、跟import标签类似,在template路径下查找
"""
app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    return render_template("include.html")


if __name__ == "__main__":
    app.run()
