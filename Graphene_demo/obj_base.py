import decimal
from datetime import datetime, date, time

import graphene
from flask import Flask
from flask_graphql.graphqlview import GraphQLView

"""
参数：
    name   重名命
    default_value='jack'    默认值
    required=True   必填项

基本数据类型
"""


class Query(graphene.ObjectType):
    """定义规则,规范"""
    hello = graphene.String(name='hi', desc=graphene.String(default_value='jack'),
                            gender=graphene.String(required=True))

    int = graphene.Int()
    float = graphene.Float()
    boolean = graphene.Boolean()
    id = graphene.ID()
    data = graphene.Date()  # data(2021.1.2)
    time = graphene.Time()  # time(1,2,3)
    date_time = graphene.DateTime()  # datetime(2021,1,2,3,4,5)
    decimal = graphene.Decimal()  # decimal(10.30)
    json = graphene.JSONString()

    def resolve_hello(self, info, desc, gender):
        """返回结果"""
        return f"hi GraphQL, desc:{desc}, gender:{gender}"

    def resolve_data(self, info):
        """返回结果"""
        return date(2021, 1, 2)

    def resolve_time(self, info):
        """返回结果"""
        return time(5, 1, 2)

    def resolve_date_time(self, info):
        """返回结果"""
        return datetime(2021, 12, 23, 4, 5, 6)

    def resolve_decimal(self, info):
        """返回结果"""
        return decimal.Decimal("20.23")

    def resolve_json(self, info):
        """返回结果"""
        return {"name": "jack"}

    info = graphene.String(required=True)

    def resolve_info(self, info):
        """返回结果"""
        return ""

    nonnull = graphene.NonNull(graphene.String)  # 不可返回为空

    def resolve_nonnull(self, info):
        """返回结果"""
        return None

    list = graphene.List(graphene.String)

    # list = graphene.List(graphene.NonNull(graphene.String)) # 不能为空写法一,限制里面的内容
    # list = graphene.NonNull(graphene.List(graphene.String))   # 不为空写法二,限制外面的内容
    def resolve_list(self, info):
        """返回结果"""
        return None


if __name__ == "__main__":
    schema = graphene.Schema(query=Query)

    app = Flask(__name__)
    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    app.run(debug=True)
