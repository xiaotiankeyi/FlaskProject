import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import graphene
from flask import Flask
from flask_graphql.graphqlview import GraphQLView
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_demo.db_tool import engine, Base
from sqlalchemy import Column
from sqlalchemy import String, Integer, Boolean, DATETIME
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
import random

"""
Graphene_sqlalchemy的使用
"""
Session = scoped_session(sessionmaker(bind=engine))
"""定义查询对象"""
Base.query = Session.query_property()


class NewAuthor(Base):
    """新闻作者表"""
    __tablename__ = "newAuthor"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(10), nullable=False)
    gender = Column(Boolean)
    age = Column(Integer)
    address = Column(String(20), default='深圳')
    createTime = Column(DATETIME, default=datetime.now)
    alterTime = Column(DATETIME, onupdate=datetime.now, default=datetime.now)

    def __repr__(self):
        return f"<id:{self.id},name:{self.name},age:{self.age},address:{self.address}>"


def insert():
    """创建数据"""
    with Session() as res:
        for a in range(20):
            name = "".join(i for i in random.sample(
                """赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许金魏陶姜戚谢邹喻柏水窦章
                云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤""", 3))
            author = NewAuthor(name=name, gender=random.choice([False, True]),
                               age=random.randint(20, 25))
            res.add(author)
        res.commit()


class DataHandle(SQLAlchemyObjectType):
    class Meta:
        model = NewAuthor


class createAuthor(graphene.Mutation):
    """定义数据的创建"""
    author = graphene.Field(DataHandle)
    fang = graphene.Boolean()

    class Arguments:
        name = graphene.String()
        gender = graphene.Boolean()
        age = graphene.Int()
        address = graphene.String()

    def mutate(self, info, name, gender, age, address):
        addData = NewAuthor(name=name, gender=gender, age=age, address=address)
        with Session() as res:
            res.add(addData)
            res.commit()
            return createAuthor(author=addData, fang=True)


class Mutation(graphene.ObjectType):
    create_author = createAuthor.Field()


class Query(graphene.ObjectType):
    """定义查询"""
    author = graphene.List(DataHandle)
    one = graphene.Field(DataHandle, id=graphene.Int())

    def resolve_author(self, info):
        """查询多个"""
        query = DataHandle.get_query(info)
        return query.all()

    def resolve_one(self, info, id):
        """查询指定的值一个值"""
        one = DataHandle.get_node(info, id)
        return one


if __name__ == '__main__':
    Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表
    # insert()

    # schema = graphene.Schema(query=Query, mutation=Mutation)
    # app = Flask(__name__)
    # app.add_url_rule('/graphql',
    #                  view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    # app.run(debug=True)
