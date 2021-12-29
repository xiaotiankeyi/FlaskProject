from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import url_for
from flask import views

"""
类视图继承views,及类视图的常见使用常景
类视图的调度
类视图装饰器
"""
app = Flask(__name__)

app.config.from_pyfile("config.py", silent=False)


@app.route("/index/")
def index():
    return render_template("parent/parent_model.html")


# 定义类视图
class classViews(views.View):
    def dispatch_request(self):
        return render_template("son_model.html")


# 注册类视图
# app.add_url_rule("/classView/", endpoint=None, view_func=classViews.as_view("classViews"))
app.add_url_rule("/classView/", endpoint="test_url_for", view_func=classViews.as_view("classViews"))


@app.route("/hello/")
def hello():
    # print(url_for("classViews"))
    print(url_for("test_url_for"))

    return "你好世界"


# 类视图使用场景1
class Jsonhandle(views.View):
    def getdate(self):
        pass

    def dispatch_request(self):
        return jsonify(self.getdate())


class Resultjson(Jsonhandle):
    def getdate(self):
        return {'name': 'jack', 'age': 22, 'address': '江西'}


app.add_url_rule('/resultjs/', view_func=Resultjson.as_view('resultjson'))


class Public(views.View):
    def __init__(self):
        self.AD = {'ad': '新东方, 好利源'}


class Page(Public):
    def dispatch_request(self):
        self.AD.update({'new_ad': '飞书, 微信'})
        # return render_template("uploadFile.html", **self.AD)
        return "公有广告:%s <br>私有广告:%s" % (self.AD['ad'], self.AD['new_ad'])


app.add_url_rule('/page/', endpoint=None, view_func=Page.as_view('/page/'))


class Login(views.MethodView):

    def __result(self):
        return render_template("son_model.html")

    def get(self):
        return self.__result()

    def post(self):
        if request.method == 'POST':
            return """登录成功后返回主页面"""
        else:
            return self.__result()

app.add_url_rule('/login/', view_func=Login.as_view("login"))


# 自定义装饰器
def judge_login(func):
    def wrapper(*args, **kwargs):
        """判断逻辑"""
        if request.args.get("username") == 'jack':
            return func()
        else:
            return "返回登录页面"

    return wrapper

# 装饰器用法一
@app.route("/family/")
@judge_login
def Myfamily():

    return "我的家园"


class Plant(views.View):
    """重写类视图的一个类属性decorators,把装饰器添加进去"""
    decorators = [judge_login]
    def dispatch_request(self):
        return "我的工厂"

app.add_url_rule("/plant/", view_func=Plant.as_view("plant"))


if __name__ == "__main__":
    app.run()
