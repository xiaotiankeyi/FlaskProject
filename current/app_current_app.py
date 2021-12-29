from flask import Flask, current_app


"""
应用上下文是存放在一个LocalStack的栈中,
和应用app相关的操作就必须要用到应用上线文
场景：获取app的名字
注意1：视图函数中不需要担心上下文的问题
"""

app = Flask(__name__)
app.config.from_pyfile('../config.py')

# 手动创建app上下文
app_current_obj = app.app_context()
# 把上下文推送到对象栈的顶部
app_current_obj.push()
print(current_app.name)

# 创建方式2
with app.app_context():
    print(current_app.name)

@app.route("/")
def index():
    print(current_app.name)
    return "<a>首页<a>"


if __name__ == "__main__":
    app.run()