from flask import Flask
from flask import render_template

"""
模板继承
1、为什么,公用的模板抽离处理放在父模板中,后面子模板直接继承,
    实现重复利用,方便修改,提高代码利用率
    调用语法：{% extends "父模板路径.html" %}
2、block语句
    一般在父模板中定义一些功能代码,子模板调用时父模板应该有能力提供一个接口
    让子模板实现具体业务的需求
        在父模板中语法 {% block 名字 %}
                       {% endblock %}  
        在子模板中语法  {% block 名字 %}
                            子模板代码
                       {% endblock %}
3、默认情况下子模板代码会覆盖父模板代码,如果想保留父模板代码,可以使用{{ super() }}
        语法   {% block 名字 %}
                    {{ super() }}
                    子模板代码
               {% endblock %}
3、在一个block模块中调用另外一个block模块的代码
        语法    {% block 名字 %}
                    {{ self.名称() }}
                    子模板代码
                {% endblock %}
4、注意事项
    1、子模板中的代码,第一行,应该是extends
    2、子模板中如果想实现自己的代码,应该放在block模块中
"""
app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    return render_template("parent/parent_model.html")


@app.route("/sonModel/")
def sonModel():
    return render_template("son_model.html")

if __name__ == "__main__":
    app.run()
