from flask import Flask
from flask import render_template

"""
宏的概念及基本使用,
1、可以传递参数,但是不能返回值
2、应用宏方式可以创建表单域常用的标签,为写html代码偷懒使用的
宏的导入及注意事项
1、实际开发中一般把宏放在一个专门的文件夹中,方便同一管理
2、导入方式一语法{% from '宏文件路经' import '宏名称' as '别名' %}
3、导入方式二语法,导入后成为了一个对象,用"别名.名称"使用{% import '宏文件路径' as '别名' %}
4、当返回的页面上的参数和宏文件共享 with context
"""
app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    return render_template("macro.html")


if __name__ == "__main__":
    app.run()
