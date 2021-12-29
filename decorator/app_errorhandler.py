from flask import Flask, g, request
from flask import redirect,render_template, abort

"""
@app.errorhandler接收状态码,可以自定义返回这种状态码的处理方式
注意1:记得返回状态码, 必须写一个参数来接收错误信息
"""

app = Flask(__name__)
# app.config.from_pyfile('../config.py')


@app.route("/", methods=['get', 'post'])
def index():
    if request.method == 'POST':
        g.name = request.form['params']
        # inputs()
        return redirect('/')
    else:
        return """
                <a>首页<a>
                <form action='/' method='post'>
                    <input type='text' name='params' value=''><br>
                    <input type='submit' value='提交'>
                <form>
                """

@app.route("/login/<username>/", methods=['get'])
def login(username):
    print('输出:',username)
    if username == '123':
        return f"值是{username}"
    else:
        abort(404)
    # return f"{username}"

@app.errorhandler(500)
def errorHandler(error):
    print(error)
    return """
            <p>处理了500的错误,返回页面<p>
            """, 500
    # return render_template("error_500.html"), 500


@app.errorhandler(404)
def paramsErroe(error):
    return "参数请求错误!!!", 404


if __name__ == "__main__":
    app.run()
