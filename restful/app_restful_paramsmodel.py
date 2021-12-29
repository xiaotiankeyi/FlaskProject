from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

app = Flask(__name__)
app.config.from_pyfile("../config.py")

api = Api(app)

"""flask-restful标准化返回参数"""


class Paraments(Resource):
    """定义参数模型"""
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
