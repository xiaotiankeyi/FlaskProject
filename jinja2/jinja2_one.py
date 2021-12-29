from flask import Flask
from flask import render_template
from flask import request

# 修改默认查找template路径
app = Flask(__name__, template_folder="templates")

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    # 适用于参数项较少时使用
    title = "学习jinja2模板"
    return render_template("index.html", title=title)


@app.route("/resultDict/")
def resultDict():
    # 适用于参数项较多时之使用转参技巧，
    context = {
        'name': 'tom',
        'age': 23,
        'gender': '男',
        'address': '广东',
        'birthday': '2021/03/23',
        'info': {
            'height': '180cm',
            'weight': '70kg'
        }
    }
    return render_template("index.html", **context)


@app.route("/resultDict2/")
def resultDict2():
    # 适用于参数项较多时,不使用转参技巧
    context = {
        'info': {
            'height': '180cm',
            'weight': '70kg'
        }
    }
    return render_template("index.html", dict=context)

@app.route("/login/")
def login():

    return "<p>我是登录页面<p>"

@app.route("/login2/<name>")
def login2(name):
    print(name)

    # 字符串传参时获取
    print(request.args.get('age'))
    print(request.args.get('address'))

    return "<p>我是登录页面<p>"

if __name__ == "__main__":
    app.run()
