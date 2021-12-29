from flask import Flask, g, request, redirect

"""
flask中常见的装饰器decorator,钩子函数
@app.before_first_request   处理项目第一次请求之前执行
@app.before_request     每次请求前就执行
@app.teardown_appcontext    不管是否有异常,注册的函数都在每次请求后执行
@app.template_filter    在使用jinja2模板的时候自定义过滤器
@app.context_processor  上下文处理器,必须返回一个字典,所有模板都可以使用字段中的值
@app.errorhandler   接收状态码,可以自定义返回状态码的响应的处理方式

"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')

@app.before_first_request
@app.before_request
@app.teardown_appcontext
@app.template_filter
@app.context_processor
@app.errorhandler
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
