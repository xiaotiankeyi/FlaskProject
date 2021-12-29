from flask import Flask
from flask import redirect
from flask import url_for
from flask import request

# 页面跳转和重定向

app = Flask(__name__)


@app.route("/login/")
def login():
    return '登陆页面'


@app.route("/profile/")
def profile():
    user = request.args.get("username")
    if user == 'soccer':
        return "登录后的页面"
    else:
        # redirect实现重定向
        # return redirect("/login/", code=302)
        return redirect(url_for("login"), code=302)


if __name__ == "__main__":
    pass
