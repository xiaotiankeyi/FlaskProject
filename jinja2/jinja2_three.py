from flask import Flask
from flask import render_template

"""
控制语句可以使用"比较运算符",也可以使用"逻辑运算符"
"""

app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    context = {
        'name': 'jack',
        'age': 23,
        'grade': 30
    }
    return render_template("if_else.html", **context)

@app.route("/forData/")
def forData():
    info = {
        'name': 'jack',
        'age': 23,
        'grade': 30
    }

    msg = ['tom', 'jack', 'lucy', 'line']

    list_dict = [
        {'name':'jack','age':23, 'address':'江西'},
        {'name':'Tom','age':25, 'address':'四川'},
        {'name':'lucy', 'age': 22, 'address': '河北'},
        {'name': 'tony', 'age': 25, 'address': '山东'},
        {'name': '盲生', 'age': 20, 'address': '安徽'},
        {'name': '剑豪', 'age': 21, 'address': '福建'}
    ]
    return render_template("for.html", info=info, msg=msg, list_dict=list_dict)


if __name__ == "__main__":
    app.run()
