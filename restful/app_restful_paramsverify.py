from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import fields
from flask_restful import inputs
from flask_restful import marshal_with
from flask_restful import reqparse

app = Flask(__name__)
app.config.from_pyfile("../config.py")

api = Api(app)

"""
flask基本上使用之参数验证
"""


# 定义视图类
class VerifyParams(Resource):

    def post(self):
        """验证用户名"""

        # 创建解析器对象
        params = reqparse.RequestParser()

        # 利用解析器添加需要验证的参数
        # required非空,trim去空格,default默认值,choices=['男','女']固定选项
        # url,regex,date转换成datetime.date数据类型
        params.add_argument('username', type=str, help='用户名验证失败',
                            required=True, trim=True)

        params.add_argument('gender', type=str, choices=['男', '女'])
        params.add_argument('url', type=inputs.url)
        params.add_argument('date', type=inputs.date)
        params.add_argument('telephone', type=inputs.regex(''))

        # 如验证成功返回合格的参数,否则报错
        args = params.parse_args()
        print(type(args))
        return {'message': '注册成功'}


# 映射url
api.add_resource(VerifyParams, "/params/", endpoint='params')

"""flask-restful标准化返回参数"""
class Paraments(Resource):

    jsonParams = {
        'title': fields.String,
        'time': fields.String,
        'context': fields.Integer
    }

    @marshal_with(jsonParams)
    def get(self):
        # return {'title': '标准化测试','time': '2021/11/4'}

        """返回方式二"""
        return obj


api.add_resource(Paraments, '/paraments/')


class NewList(object):
    def __init__(self, title, context):
        self.title = title
        self.context = context


obj = NewList('class对象', 3233)

if __name__ == "__main__":
    app.run()
