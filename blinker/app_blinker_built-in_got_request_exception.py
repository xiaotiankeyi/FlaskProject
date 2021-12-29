from flask import Flask, g, request, redirect,got_request_exception
"""
flask内置信号一共10个
6、got_request_exception     请求过程中发生异常时发送信号

"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')


@app.route("/", methods=['get', 'post'])
def index():
    if request.method == 'POST':
        g.name = request.form['params']
        input()
        return redirect('/')
    else:
        return """
                <a>首页<a>
                <form action='/' method='post'>
                    <input type='text' name='params' value=''><br>
                    <input type='submit' value='提交'>
                <form>
                <a href="/result/">点击跳转<a>
                """

def requestError(sender, exception):
    """实现把函数报错信息记录日志中"""
    print(sender)
    print(exception)
    with open("./funcError.txt", mode='a') as f:
        errorData = f"{sender}视图函数执行时报{exception}错误"
        f.write(errorData+"\n")
        f.close()


got_request_exception.connect(requestError)

@app.route("/result/")
def result():
    """测试,制造一个bug"""
    a = 1/0
    return "跳转后的响应!!!"


if __name__ == "__main__":
    app.run()
