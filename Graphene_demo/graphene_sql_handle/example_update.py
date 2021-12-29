import graphene
import pymysql
from flask import Flask
from flask_graphql.graphqlview import GraphQLView

"""
Graphene和数据库结合使用,使用SQL语句更新数据
"""


def db_tool():
    db = pymysql.connect(
        host='192.168.0.121',
        port=3306,
        user='mysql',
        passwd='123456',
        db='sqlALchemy',
        charset='utf8')

    obj = db.cursor(cursor=pymysql.cursors.DictCursor)

    return db, obj


class Author(graphene.ObjectType):
    """定义数据字段及类型,可以同步数据库里面数据字段"""
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.Boolean()
    age = graphene.Int()
    address = graphene.String()
    createTime = graphene.DateTime()
    alterTime = graphene.DateTime()


class updateAuthor(graphene.Mutation):
    class Arguments:
        id = graphene.Int()
        name = graphene.String()
        gender = graphene.Boolean()
        age = graphene.Int()
        address = graphene.String()

    fang = graphene.Boolean()

    def mutate(self, info, id, name, gender, age, address):
        sql = "update newAuthor set name=%s, gender=%s, age=%s, address=%s where id=%s"
        db, obj = db_tool()
        obj.execute(sql, (name, gender, age, address, id))
        db.commit()
        db.close()
        """返回添加结果"""
        return updateAuthor(fang=True)


class DataInput(graphene.InputObjectType):
    id = graphene.Int()
    name = graphene.String()
    gender = graphene.Boolean()
    age = graphene.Int()
    address = graphene.String()


class updateAuthor2(graphene.Mutation):
    class Arguments:
        data_input = DataInput()

    fang = graphene.Boolean()

    def mutate(self, info, data_input):
        sql = "update newAuthor set name=%s, gender=%s, age=%s, address=%s where id=%s"
        db, obj = db_tool()
        obj.execute(sql, (data_input.get('name'), data_input.get('gender'), data_input.get('age'),
                          data_input.get('address'), data_input.get('id')))
        db.commit()
        db.close()
        """返回添加结果"""
        return updateAuthor2(fang=True)


class Mutation(graphene.ObjectType):
    update_author = updateAuthor.Field()
    update_author2 = updateAuthor2.Field()

class Query(graphene.ObjectType):
    """定义查询"""
    author = graphene.List(Author)

    def resolve_author(self, info):
        db, obj = db_tool()

        sql = "select * from newAuthor;"
        obj.execute(sql)
        """查询后返回所有行"""
        val = obj.fetchall()
        db.close()
        author = []
        for v in val:
            author.append(Author(id=v['id'], name=v['name'], gender=v['gender'],
                                 age=v['age'], address=v['address'], createTime=v['createTime'],
                                 alterTime=v['alterTime']
                                 ))
        return author


if __name__ == '__main__':
    schema = graphene.Schema(query=Query, mutation=Mutation)
    app = Flask(__name__)
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)

"""
mutation{
  updateAuthor(id:1,name:"赖志天",age:22, gender:true,address:"江西"){
    fang
  }
}

mutation{
  updateAuthor2(dataInput:{name:"小熊饼干",age:22,gender:false,address:"深圳",id:2}){
    fang
  }
}
"""
