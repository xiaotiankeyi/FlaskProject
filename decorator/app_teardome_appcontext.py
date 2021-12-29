from flask import Flask, g, request, redirect

"""
@app.teardown_appcontext

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

@app.teardown_appcontext
def teardown_appcontext(exc=None):
    if exc == None:
        if request.method == 'get':
            print('为get请请求')
        else:
            print('为post请求')
    else:
        print("存在错误!!")

if __name__ == "__main__":
    app.run()
