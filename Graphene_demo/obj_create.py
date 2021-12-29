import graphene
from flask import Flask
from flask_graphql import GraphQLView

"""
Graphene增加数据
"""

user = []


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


class createPerson(graphene.Mutation):
    person = graphene.Field(Person)
    msg = graphene.String()

    class Arguments:
        """定义前端可以传递的参数"""
        name = graphene.String()
        age = graphene.Int()

    def mutate(self, info, name, age):
        """定义存储的逻辑"""
        p = Person(name=name, age=age)
        user.append(p)

        """定义响应请求逻辑"""
        return createPerson(person=p, msg="success")


class Mutation(graphene.ObjectType):
    """映射对外使用字段,注册"""
    create_person = createPerson.Field()


class Query(graphene.ObjectType):
    persons = graphene.List(Person)

    def resolve_persons(self, info):
        return user


if __name__ == '__main__':
    schema = graphene.Schema(query=Query, mutation=Mutation)
    app = Flask(__name__)
    app.add_url_rule('/graphql',
                     view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
    app.run(debug=True)

"""
增加及查询方式
mutation ap{
  createPerson(name:"jakc", age:22){
    person{
      name
      age
    }
    msg
  }
}

query cp{
  persons{
    name
  }
}
"""