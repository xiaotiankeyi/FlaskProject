import graphene
from flask import Flask
from flask_graphql import GraphQLView

"""
Graphene修改数据
"""


class Person(graphene.ObjectType):
    name = graphene.String()
    age = graphene.Int()


user = [
    Person(name='jack', age=22),
    Person(name='lucy', age=25)
]


class updatePerson(graphene.Mutation):
    person = graphene.Field(Person)
    msg = graphene.String()

    class Arguments:
        """定义前端可以传递的参数"""
        name = graphene.String()
        age = graphene.Int()

    def mutate(self, info, name, age):
        for i in user:
            """通过判断前端传过里的名字来修改年龄"""
            if i.name == name:
                i.age = age
                return updatePerson(person=i, msg="success")
        return updatePerson(msg="Did not find")


class Mutation(graphene.ObjectType):
    """映射对外使用字段,注册"""
    update_person = updatePerson.Field()


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
修改及查询写法
query qa{
  persons{
    name
    age
  }
}
修改写法
mutation cp{
  updatePerson(name:"jack", age:21){
  msg
  }
}
"""
