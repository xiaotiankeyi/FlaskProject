from flask import Flask
from flask import render_template

"""
set和with语句以及模板中定义变量
1、在模板中可以用set语句定义变量，类似全局变量
    语法 {% set name='jack' %}
    引用 <p>{{ name }}<p>
2、with语句定义的变量,只能在with语句块中使用,类似局部变量
    语法 {% with classroom='python' %}
            <p>{{ classroom }}<p>
         {% endwith %}
3、注意事项,如set语句在with语句中定义后,就会变为局部变量
"""
app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    return render_template("set_with.html")


@app.route("/loadStatic/")
def loadStatic():
    return render_template("static_file.html")

if __name__ == "__main__":
    app.run()
