from flask import Flask
from flask import render_template
from flask import url_for

from blueprint.app_restful_Newparamsmodel import newDataModel
from blueprint.flask_nine import app_user  # 导入蓝图文件及对象
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# 注册蓝图
app.register_blueprint(app_user)
app.register_blueprint(newDataModel)


@app.route("/")
def index():
    """使用url_for构建蓝图中的函数,先指定蓝图名称+视图函数名"""
    print(url_for("user_info.user"))
    # return "<p>hello world<p>"
    return render_template("page.html")

# 创建migrate对象
from migrate_demo import application
Migrate(app=app, db=db)
# print('被调用')

if __name__ == "__main__":
    app.run()
