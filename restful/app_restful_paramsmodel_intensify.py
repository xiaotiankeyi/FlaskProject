from flask import Flask
from flask_restful import Api
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

app = Flask(__name__)
app.config.from_pyfile("../config.py")

api = Api(app)

"""
flask-restful标准化返回参数,对参数模型的强化
"""


class Paraments(Resource):
    """定义参数模型"""
    jsonParams = {
        # 重命名属性
        'title': fields.String(attribute='titleInfo'),
        'time': fields.String,
        'context': fields.Integer,
        'message': fields.String
        # 'message':fields.String(default='默认值,什么都没有')
    }

    @marshal_with(jsonParams)
    def get(self):
        return {'titleInfo': '标准化测试','time': '2021/11/4'}

        # 返回方式二
        # return obj


api.add_resource(Paraments, '/paraments/')


class NewList(object):
    def __init__(self, titleInfo, context):
        self.titleInfo = titleInfo
        self.context = context


obj = NewList('class对象', 3233)

if __name__ == "__main__":
    app.run()
