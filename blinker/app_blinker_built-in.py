from flask import Flask, g, request, redirect
"""
flask内置信号一共10个
1、template_rendered     模板渲染完成后的信号
2、before_render_template    模板渲染之前的信号
3、request_started   请求开始之前,到达视图函数时发出信号
4、request_finished     请求结束时,在响应发送给客服端之前发送信号
5、request_tearing_down     请求对象被销毁时发送的信号,异常请求也会发送信号
6、got_request_exception     请求过程中发生异常时发送信号
7、appcontext_tearing_down   应用上下文被销毁时发送的信号
8、appcontext_pushed     应用上下文被推入到栈上时发送的信号
9、appcontext_poped      应用上下文被推出栈时发送的信号
10、message_flashed      调用了Flask的'flash'方式时发送的信号 
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
                """


def input():
    print("输出前端数据:", g.name)


if __name__ == "__main__":
    app.run()
