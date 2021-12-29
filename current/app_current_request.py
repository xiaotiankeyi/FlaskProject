from flask import Flask, current_app,url_for


"""
请求上下文是存放在一个LocalStack的栈中,
请求相关的操作就必须用到请求上下文

"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')



@app.route("/index/")
def index():
    print(current_app.name)
    return "<a>首页<a>"

# 手动推入请求上下文到栈内存中
with app.test_request_context():
    print(url_for('index'))


if __name__ == "__main__":
    app.run()