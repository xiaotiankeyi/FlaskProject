from flask import Blueprint
from flask_restful import Api
from flask_restful import Resource
from flask_restful import fields
from flask_restful import marshal_with

"""
flask-restful结合蓝图的使用
"""

newDataModel = Blueprint('newData', __name__, url_prefix='/news')
api = Api(newDataModel)     # 在蓝图里Api函数继承蓝图对象


class NewUser(object):
    def __init__(self, name, gender, age, address):
        self.name = name
        self.gender = gender
        self.age = age
        self.address = address

    def __repr__(self):
        return f"查询的用户信息为{self.name},{self.gender}," \
            f"{self.age}, {self.address}"


class NewContext(object):
    def __init__(self, id, context):
        self.newId = id
        self.context = context
        self.author = None
        self.tags = []

    def __repr__(self):
        return f"新闻信息为{self.newId},{self.author}, {self.context}, {self.tags}"


class NewTags(object):
    def __init__(self, TagId, TagName):
        self.tid = TagId
        self.tName = TagName

    def __repr__(self):
        return f"标签信息为{self.tid}, {self.tName}"


def NewData():
    """组织新闻信息"""
    user = NewUser('路遥', '男', 50, '陕西')
    tag1 = NewTags(2001, '文学')
    tag2 = NewTags(2002, '名著')
    contextObj = NewContext(1001, '平凡的世界')
    contextObj.author = user
    contextObj.tags.append(tag1)
    contextObj.tags.append(tag2)
    # print(contextObj)

    return contextObj


class NewDataModel(Resource):
    """定义新闻数据参数模型"""
    jsonParams = {
        'newId': fields.Integer,
        'context': fields.String,
        'author': fields.Nested({
            'name': fields.String,
            'gender': fields.String,
            'age': fields.Integer,
            'address': fields.String
        }),

        'tags': fields.List(fields.Nested({
            'tid': fields.Integer,
            'tName': fields.String
        }))
    }

    @marshal_with(jsonParams)
    def get(self):
        # 返回方式二
        obj = NewData()
        return obj


api.add_resource(NewDataModel, '/newData/')

if __name__ == "__main__":
    pass
