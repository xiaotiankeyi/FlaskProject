from flask import Flask
from flask import request
from flask import url_for
from werkzeug.routing import BaseConverter
from flask import redirect

app = Flask(__name__)

# 导入配置
# app.config.from_object("")
app.config.from_pyfile("config.py", silent=False)


@app.route('/')
def hello_world():
    # return 'Hello World!'
    return url_for('list_func', id=3)


# @app.route('/result/<id>/')
# @app.route('/result/<string:id>/')
# @app.route('/result/<int:id>/')     指定返回参数类型
@app.route('/<any(result,return):url_path>/<id>/')
def result(url_path, id):
    return '页面返回的id %s' % id


@app.route('/params/', methods=['get', 'post'])
def params():
    if request.method == 'GET':
        # 获取get请求的参数
        get_value = request.args.get('name')
        return '返回获取得参数 %s' % get_value

    if request.method == 'POST':
        # 获取post请求的参数
        post_value = request.form['name']
        post_value = request.form.get('name')
        return '返回获取得参数 %s' % post_value


@app.route('/list/<id>')
def list_func(id):
    print('被调用')

    return 'url_for的应用'


# 自定义url转换器之电话号码匹配
class TelephoneConverter(BaseConverter):
    regex = "1[345789]\d{9}"


app.url_map.converters['phone'] = TelephoneConverter

# to_python和to_url的使用

class Toconverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

app.url_map.converters['to'] = Toconverter

@app.route("/testTo/<to:module>/")
def testTo(module):
    print(module)
    return "页面返回的值是 %s" % module


if __name__ == '__main__':
    app.run()

    # 开启debug模式
    # app.debug = True
    # app.config.update(DEBUG=True)
    # app.run(debug=True)
    pass
