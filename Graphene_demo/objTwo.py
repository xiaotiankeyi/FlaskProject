import graphene
from flask import Flask
from flask_graphql.graphqlview import GraphQLView
from graphene import String, Int, Boolean

"""
自定义数据类型
"""


class Person(graphene.ObjectType):
    """定义创建对象 """
    name = String()
    age = Int()
    gender = Boolean()


class Query(graphene.ObjectType):
    # 自定义返回数据类型
    person = graphene.Field(Person)

    def resolve_person(self, info):
        """返回字典"""
        return {"name": "jack", "age": 34, "gender": False, "address": "江西"}

    """自定义返回列表"""
    personList = graphene.List(Person)

    def resolve_personList(self, info):
        return [
            {"name": "jack", "age": 34, "gender": False},
            {"name": "Tom", "age": 24, "gender": True}
        ]


if __name__ == "__main__":
    schema = graphene.Schema(query=Query)

    app = Flask(__name__)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    app.run(debug=True)
