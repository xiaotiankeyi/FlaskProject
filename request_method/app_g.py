from flask import Flask, g, request, redirect

"""
g全局的作用：
    将一些经常使用的数据绑定到上面,以后就直接从g上面取就可以了
    而不需要通过传参的方式
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
