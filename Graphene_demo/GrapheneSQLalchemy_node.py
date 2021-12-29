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
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
import random

"""
Graphene_sqlalchemy中node的查询
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
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    """定义查询"""
    node = graphene.relay.Node.Field()
    emps = SQLAlchemyConnectionField(DataHandle.connection)


if __name__ == '__main__':
    # Base.metadata.drop_all()  # 删除表
    # Base.metadata.create_all()  # 创建表
    # insert()

    schema = graphene.Schema(query=Query)
    app = Flask(__name__)
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)

"""
1、查询写法,DataHandle+id进行base64编码在进行查找
{node(id:"RGF0YUhhbmRsZToy"){
  	... on DataHandle{
    	id
    	name
    	gender
      age
      createTime
      alterTime
      address
  }
}}

2、arrayconnection:4进行base64编码,查询前面4个
query rd{
  emps(sort:ID_DESC, before:"YXJyYXljb25uZWN0aW9uOjQ=") {
    edges {
      node {
        id
        name
      }
    }
  }
}

3、取前面4条数据,在4条数据中取后面两条数据
query pm{
  emps(sort:ID_DESC, before:"YXJyYXljb25uZWN0aW9uOjQ=",first:2) {
    edges {
      node {
        id
        name
      }
    }
  }
}
"""